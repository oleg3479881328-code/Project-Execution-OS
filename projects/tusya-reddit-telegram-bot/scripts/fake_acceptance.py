from __future__ import annotations

import asyncio
import json
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path

from tusya_bot.ai.client import DraftResult
from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.db.repositories import (
    KeywordRepository,
    PostRepository,
    ResourceRepository,
)
from tusya_bot.delivery.fake import CollectingDeliveryService
from tusya_bot.domain.enums import MatchMode
from tusya_bot.domain.models import MonitoredResource
from tusya_bot.monitoring.engine import MonitoringEngine
from tusya_bot.reddit.client import RedditFetchedPost
from tusya_bot.services.draft_service import DraftService
from tusya_bot.services.keyword_service import KeywordService
from tusya_bot.services.post_service import PostService
from tusya_bot.services.resource_service import ResourceService


@dataclass
class FakeDraftClient:
    counter: int = 0

    async def create_draft(self, request):  # type: ignore[no-untyped-def]
        self.counter += 1
        suffix = f"revision-{self.counter}"
        return DraftResult(
            text=f"Draft for {request.title} [{suffix}]",
            provider="deepseek-fake",
            model="deepseek-v4-flash",
            prompt_version="reddit-reply-v1",
        )


class FakeRedditClient:
    def __init__(self, responses: list[list[RedditFetchedPost]]) -> None:
        self._responses = responses

    async def fetch_posts(
        self,
        resource: MonitoredResource,
        *,
        limit: int = 25,
    ) -> list[RedditFetchedPost]:
        del resource, limit
        return self._responses.pop(0)


async def run_acceptance() -> dict[str, object]:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        database = Database(root / "data" / "tusya.sqlite3")
        async with database.connect() as connection:
            await migrate(connection)

        resource_service = ResourceService(database)
        keyword_service = KeywordService(database)
        post_service = PostService(database)
        draft_service = DraftService(database=database, client=FakeDraftClient())

        resource = await resource_service.add_resource("r/WedditNYC")
        await keyword_service.add_keyword("photography", match_mode=MatchMode.CONTAINS)

        start = datetime(2026, 7, 13, 20, 0, tzinfo=UTC)
        responses = [
            [
                RedditFetchedPost(
                    reddit_id="old-1",
                    subreddit="WedditNYC",
                    title="Old planning thread",
                    body="already there",
                    permalink="https://reddit.example/old-1",
                    author="user1",
                    created_utc=start.isoformat(),
                )
            ],
            [
                RedditFetchedPost(
                    reddit_id="old-1",
                    subreddit="WedditNYC",
                    title="Old planning thread",
                    body="already there",
                    permalink="https://reddit.example/old-1",
                    author="user1",
                    created_utc=start.isoformat(),
                ),
                RedditFetchedPost(
                    reddit_id="new-1",
                    subreddit="WedditNYC",
                    title="Need photography help",
                    body="Brooklyn wedding this fall",
                    permalink="https://reddit.example/new-1",
                    author="user2",
                    created_utc=(start + timedelta(minutes=5)).isoformat(),
                ),
            ],
            [
                RedditFetchedPost(
                    reddit_id="old-1",
                    subreddit="WedditNYC",
                    title="Old planning thread",
                    body="already there",
                    permalink="https://reddit.example/old-1",
                    author="user1",
                    created_utc=start.isoformat(),
                ),
                RedditFetchedPost(
                    reddit_id="new-1",
                    subreddit="WedditNYC",
                    title="Need photography help",
                    body="Brooklyn wedding this fall",
                    permalink="https://reddit.example/new-1",
                    author="user2",
                    created_utc=(start + timedelta(minutes=5)).isoformat(),
                ),
            ],
        ]
        delivery = CollectingDeliveryService()
        engine = MonitoringEngine(
            database=database,
            reddit_client=FakeRedditClient(responses),
            delivery_service=delivery,
            poll_interval_seconds=300,
            now_fn=lambda: start,
            jitter_fn=lambda _: 0.0,
        )

        baseline = await engine.run_cycle(trigger="manual")
        second = await engine.run_cycle(trigger="manual")

        delivered_post_id = delivery.emitted[0].post.id or 0
        opened_post = await post_service.mark_opened(delivered_post_id)
        first_draft = await draft_service.create_draft(delivered_post_id)
        second_draft = await draft_service.regenerate_draft(delivered_post_id)
        third_draft = await draft_service.refine_draft(
            delivered_post_id,
            "сделай короче и теплее",
        )
        await draft_service.update_preferences(
            language="Russian",
            tone="warm and short",
            max_words=90,
        )

        restarted_post_service = PostService(database)
        restarted_draft_service = DraftService(database=database, client=FakeDraftClient())
        persisted_post = await restarted_post_service.get_post(delivered_post_id)
        persisted_drafts = await restarted_draft_service.list_drafts(delivered_post_id)
        duplicate = await engine.run_cycle(trigger="manual")

        async with database.connect() as connection:
            resource_count = len(await ResourceRepository(connection).list_all())
            keyword_count = len(await KeywordRepository(connection).list_all())
            stored_posts = await PostRepository(connection).list_by_resource(resource.id or 0)

        return {
            "resource_count": resource_count,
            "keyword_count": keyword_count,
            "stored_post_ids": [post.reddit_id for post in stored_posts],
            "baseline_candidates": baseline.emitted_candidates,
            "second_candidates": second.emitted_candidates,
            "delivery_cards": len(delivery.emitted),
            "opened_status": opened_post.status.value,
            "draft_ids": [first_draft.id, second_draft.id, third_draft.id],
            "persisted_draft_count": len(persisted_drafts),
            "persisted_post_status": persisted_post.status.value,
            "duplicate_candidates": duplicate.emitted_candidates,
        }


def main() -> int:
    result = asyncio.run(run_acceptance())
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    assert result["baseline_candidates"] == 0
    assert result["second_candidates"] == 1
    assert result["delivery_cards"] == 1
    assert result["persisted_draft_count"] == 3
    assert result["duplicate_candidates"] == 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
