from __future__ import annotations

import asyncio
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.db.repositories import KeywordRepository, PostRepository, ResourceRepository
from tusya_bot.delivery.fake import CollectingDeliveryService
from tusya_bot.domain.enums import MatchMode, ResourceType
from tusya_bot.domain.models import Keyword, MonitoredResource
from tusya_bot.monitoring.engine import MonitoringEngine
from tusya_bot.reddit.client import RedditFetchedPost


class FakeRedditClient:
    def __init__(self, responses: dict[int, list[object]]) -> None:
        self._responses = responses

    async def fetch_posts(
        self,
        resource: MonitoredResource,
        *,
        limit: int = 25,
    ) -> list[RedditFetchedPost]:
        del limit
        response = self._responses[resource.id or 0].pop(0)
        if isinstance(response, Exception):
            raise response
        assert isinstance(response, list)
        return list(response)


class SlowRedditClient:
    def __init__(self) -> None:
        self.started = asyncio.Event()
        self.release = asyncio.Event()

    async def fetch_posts(
        self,
        resource: MonitoredResource,
        *,
        limit: int = 25,
    ) -> list[RedditFetchedPost]:
        del resource, limit
        self.started.set()
        await self.release.wait()
        return []


def _fetched_post(
    reddit_id: str,
    *,
    title: str,
    body: str = "",
    created_at: datetime,
) -> RedditFetchedPost:
    return RedditFetchedPost(
        reddit_id=reddit_id,
        subreddit="WedditNYC",
        title=title,
        body=body,
        permalink=f"https://www.reddit.com/r/WedditNYC/comments/{reddit_id}/post/",
        author="tester",
        created_utc=created_at.isoformat(),
    )


async def _seed_resource(
    database: Database,
    *,
    canonical_url: str,
    baseline_completed: bool = False,
    next_check_at: str | None = None,
) -> MonitoredResource:
    async with database.connect() as connection:
        return await ResourceRepository(connection).create(
            MonitoredResource(
                id=None,
                original_input=canonical_url,
                canonical_url=canonical_url,
                subreddit="WedditNYC",
                resource_type=(
                    ResourceType.SEARCH if "/search/" in canonical_url else ResourceType.SUBREDDIT
                ),
                search_query="photographer" if "/search/" in canonical_url else None,
                sort_mode="new",
                baseline_completed=baseline_completed,
                next_check_at=next_check_at,
            )
        )


async def _seed_keyword(database: Database, keyword: str) -> None:
    async with database.connect() as connection:
        await KeywordRepository(connection).create(
            Keyword(
                id=None,
                keyword=keyword,
                normalized_keyword=keyword.casefold(),
                match_mode=MatchMode.CONTAINS,
            )
        )


@pytest.fixture
async def prepared_database(tmp_path: Path) -> Database:
    database = Database(tmp_path / "tusya.sqlite3")
    async with database.connect() as connection:
        await migrate(connection)
    return database


@pytest.mark.asyncio
async def test_first_baseline_sends_zero_candidates(prepared_database: Database) -> None:
    resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
    )
    await _seed_keyword(prepared_database, "photographer")
    delivery = CollectingDeliveryService()
    now = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=FakeRedditClient(
            {resource.id or 0: [[_fetched_post("a1", title="photographer", created_at=now)]]}
        ),
        delivery_service=delivery,
        poll_interval_seconds=300,
        now_fn=lambda: now,
        jitter_fn=lambda _: 0.0,
    )

    result = await engine.run_cycle(trigger="manual")

    assert result.emitted_candidates == 0
    assert delivery.emitted == []
    async with prepared_database.connect() as connection:
        resources = await ResourceRepository(connection).list_all()
        posts = await PostRepository(connection).list_by_resource(resource.id or 0)
    assert resources[0].baseline_completed is True
    assert [post.reddit_id for post in posts] == ["a1"]


@pytest.mark.asyncio
async def test_second_poll_with_one_unseen_matching_post_emits_exactly_one_candidate(
    prepared_database: Database,
) -> None:
    resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
    )
    await _seed_keyword(prepared_database, "photographer")
    delivery = CollectingDeliveryService()
    start = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=FakeRedditClient(
            {
                resource.id or 0: [
                    [_fetched_post("a1", title="Old post", created_at=start)],
                    [
                        _fetched_post("a1", title="Old post", created_at=start),
                        _fetched_post(
                            "a2",
                            title="Need photographer soon",
                            created_at=start + timedelta(minutes=5),
                        ),
                    ],
                ]
            }
        ),
        delivery_service=delivery,
        poll_interval_seconds=300,
        now_fn=lambda: start,
        jitter_fn=lambda _: 0.0,
    )

    await engine.run_cycle(trigger="manual")
    second_result = await engine.run_cycle(trigger="manual")

    assert second_result.emitted_candidates == 1
    assert [candidate.post.reddit_id for candidate in delivery.emitted] == ["a2"]
    assert delivery.emitted[0].matched_keywords == ("photographer",)


@pytest.mark.asyncio
async def test_unseen_nonmatching_post_is_stored_but_not_emitted(
    prepared_database: Database,
) -> None:
    resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
    )
    await _seed_keyword(prepared_database, "photographer")
    delivery = CollectingDeliveryService()
    start = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=FakeRedditClient(
            {
                resource.id or 0: [
                    [],
                    [_fetched_post("b1", title="Venue question", created_at=start)],
                ]
            }
        ),
        delivery_service=delivery,
        poll_interval_seconds=300,
        now_fn=lambda: start,
        jitter_fn=lambda _: 0.0,
    )

    await engine.run_cycle(trigger="manual")
    second_result = await engine.run_cycle(trigger="manual")

    assert second_result.emitted_candidates == 0
    assert delivery.emitted == []
    async with prepared_database.connect() as connection:
        posts = await PostRepository(connection).list_by_resource(resource.id or 0)
    assert [post.reddit_id for post in posts] == ["b1"]
    assert json.loads(posts[0].matched_keywords_json) == []


@pytest.mark.asyncio
async def test_duplicate_poll_emits_nothing(prepared_database: Database) -> None:
    resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
    )
    await _seed_keyword(prepared_database, "photographer")
    delivery = CollectingDeliveryService()
    start = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
    matching_post = _fetched_post("c1", title="photographer needed", created_at=start)
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=FakeRedditClient(
            {
                resource.id or 0: [
                    [],
                    [matching_post],
                    [matching_post],
                ]
            }
        ),
        delivery_service=delivery,
        poll_interval_seconds=300,
        now_fn=lambda: start,
        jitter_fn=lambda _: 0.0,
    )

    await engine.run_cycle(trigger="manual")
    first = await engine.run_cycle(trigger="manual")
    second = await engine.run_cycle(trigger="manual")

    assert first.emitted_candidates == 1
    assert second.emitted_candidates == 0
    assert [candidate.post.reddit_id for candidate in delivery.emitted] == ["c1"]


@pytest.mark.asyncio
async def test_one_failed_resource_does_not_block_another(
    prepared_database: Database,
) -> None:
    bad_resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/search/?q=photographer&type=posts&sort=new",
    )
    good_resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
        baseline_completed=True,
    )
    await _seed_keyword(prepared_database, "photographer")
    delivery = CollectingDeliveryService()
    start = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=FakeRedditClient(
            {
                bad_resource.id or 0: [RuntimeError("reddit timeout")],
                good_resource.id or 0: [
                    [
                        _fetched_post(
                            "d1",
                            title="photographer available",
                            created_at=start + timedelta(minutes=1),
                        )
                    ]
                ],
            }
        ),
        delivery_service=delivery,
        poll_interval_seconds=300,
        now_fn=lambda: start,
        jitter_fn=lambda _: 0.0,
    )

    result = await engine.run_cycle(trigger="manual")

    assert result.failed_resources == 1
    assert result.emitted_candidates == 1
    assert [candidate.post.reddit_id for candidate in delivery.emitted] == ["d1"]


@pytest.mark.asyncio
async def test_no_overlapping_cycles(prepared_database: Database) -> None:
    resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
    )
    slow_client = SlowRedditClient()
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=slow_client,
        delivery_service=CollectingDeliveryService(),
        poll_interval_seconds=300,
        now_fn=lambda: datetime(2026, 7, 13, 20, 0, tzinfo=UTC),
        jitter_fn=lambda _: 0.0,
    )

    task = asyncio.create_task(engine.run_cycle(trigger="manual"))
    await slow_client.started.wait()
    overlapping = await engine.run_cycle(trigger="manual")
    slow_client.release.set()
    first_result = await task

    assert resource.id is not None
    assert overlapping.overlap_skipped is True
    assert first_result.overlap_skipped is False


@pytest.mark.asyncio
async def test_backoff_metadata_updates(prepared_database: Database) -> None:
    resource = await _seed_resource(
        prepared_database,
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
    )
    now = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
    engine = MonitoringEngine(
        database=prepared_database,
        reddit_client=FakeRedditClient({resource.id or 0: [RuntimeError("rate limited")]}),
        delivery_service=CollectingDeliveryService(),
        poll_interval_seconds=300,
        now_fn=lambda: now,
        jitter_fn=lambda _: 0.0,
    )

    await engine.run_cycle(trigger="manual")

    async with prepared_database.connect() as connection:
        updated = (await ResourceRepository(connection).list_all())[0]
    assert updated.failure_count == 1
    assert updated.last_error == "rate limited"
    assert updated.next_check_at == (now + timedelta(seconds=300)).isoformat()
