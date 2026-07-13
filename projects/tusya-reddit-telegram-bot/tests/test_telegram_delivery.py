from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace

import pytest
from telegram.error import TelegramError

from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.db.repositories import DeliveryEventRepository, PostRepository, ResourceRepository
from tusya_bot.delivery.telegram import TelegramDeliveryService
from tusya_bot.domain.enums import DeliveryStatus, PostStatus, ResourceType
from tusya_bot.domain.models import MonitoredResource, RedditPost
from tusya_bot.monitoring.models import DeliveryCandidate
from tusya_bot.services.post_service import PostService


class _SuccessfulBot:
    def __init__(self) -> None:
        self.calls = 0

    async def send_message(self, **kwargs: object) -> SimpleNamespace:
        self.calls += 1
        return SimpleNamespace(message_id=555, **kwargs)


class _FailingBot:
    async def send_message(self, **kwargs: object) -> SimpleNamespace:
        del kwargs
        raise TelegramError("forbidden")


@pytest.fixture
async def delivery_database(tmp_path: Path) -> Database:
    database = Database(tmp_path / "delivery.sqlite3")
    async with database.connect() as connection:
        await migrate(connection)
    return database


async def _persist_post(database: Database) -> RedditPost:
    resource = MonitoredResource(
        id=None,
        original_input="https://www.reddit.com/r/WedditNYC/new/",
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
        subreddit="WedditNYC",
        resource_type=ResourceType.SUBREDDIT,
        search_query=None,
        sort_mode="new",
    )
    async with database.connect() as connection:
        saved_resource = await ResourceRepository(connection).create(resource)
        resource_id = saved_resource.id or 0
        return await PostRepository(connection).create(
            RedditPost(
                id=None,
                reddit_id="abc123",
                resource_id=resource_id,
                subreddit="WedditNYC",
                title="Need photographer",
                body="Brooklyn wedding.",
                permalink="https://www.reddit.com/r/WedditNYC/comments/abc123/post/",
                author="owner",
                created_utc=datetime(2026, 7, 13, 21, 0, tzinfo=UTC).isoformat(),
                matched_keywords_json='["photographer"]',
                status=PostStatus.NEW,
            )
        )


def _candidate(post: RedditPost) -> DeliveryCandidate:
    resource = MonitoredResource(
        id=1,
        original_input="https://www.reddit.com/r/WedditNYC/new/",
        canonical_url="https://www.reddit.com/r/WedditNYC/new/",
        subreddit="WedditNYC",
        resource_type=ResourceType.SUBREDDIT,
        search_query=None,
        sort_mode="new",
    )
    return DeliveryCandidate(
        resource=resource,
        post=post,
        matched_keywords=("photographer",),
    )


@pytest.mark.asyncio
async def test_delivery_success_persistence(delivery_database: Database) -> None:
    post = await _persist_post(delivery_database)
    service = TelegramDeliveryService(
        bot=_SuccessfulBot(),  # type: ignore[arg-type]
        owner_chat_id=1001,
        post_service=PostService(delivery_database),
    )

    await service.deliver_candidates([_candidate(post)])

    async with delivery_database.connect() as connection:
        saved_post = await PostRepository(connection).get_by_id(post.id or 0)
        events = await DeliveryEventRepository(connection).list_by_post_id(post.id or 0)
    assert saved_post is not None
    assert saved_post.delivered_at is not None
    assert len(events) == 1
    assert events[0].delivery_status == DeliveryStatus.DELIVERED
    assert events[0].telegram_message_id == "555"


@pytest.mark.asyncio
async def test_delivery_failure_persistence(delivery_database: Database) -> None:
    post = await _persist_post(delivery_database)
    service = TelegramDeliveryService(
        bot=_FailingBot(),  # type: ignore[arg-type]
        owner_chat_id=1001,
        post_service=PostService(delivery_database),
    )

    await service.deliver_candidates([_candidate(post)])

    async with delivery_database.connect() as connection:
        saved_post = await PostRepository(connection).get_by_id(post.id or 0)
        events = await DeliveryEventRepository(connection).list_by_post_id(post.id or 0)
    assert saved_post is not None
    assert saved_post.delivered_at is None
    assert len(events) == 1
    assert events[0].delivery_status == DeliveryStatus.FAILED
    assert events[0].error == "Telegram delivery failed."


@pytest.mark.asyncio
async def test_retry_without_duplicate_notification(delivery_database: Database) -> None:
    post = await _persist_post(delivery_database)
    bot = _SuccessfulBot()
    service = TelegramDeliveryService(
        bot=bot,  # type: ignore[arg-type]
        owner_chat_id=1001,
        post_service=PostService(delivery_database),
    )

    await service.deliver_candidates([_candidate(post)])
    await service.deliver_candidates([_candidate(post)])

    async with delivery_database.connect() as connection:
        events = await DeliveryEventRepository(connection).list_by_post_id(post.id or 0)
    assert bot.calls == 1
    assert len(events) == 1
