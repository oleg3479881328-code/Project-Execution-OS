from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import pytest

from tusya_bot.ai.client import DraftResult
from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.db.repositories import DraftRepository, PostRepository, ResourceRepository
from tusya_bot.domain.enums import PostStatus, ResourceType
from tusya_bot.domain.errors import DraftGenerationError
from tusya_bot.domain.models import MonitoredResource, RedditPost
from tusya_bot.services.draft_service import DraftService


@dataclass
class _FakeClient:
    text: str = "Draft reply text"

    async def create_draft(self, request):  # type: ignore[no-untyped-def]
        self.last_request = request
        return DraftResult(
            text=self.text,
            provider="deepseek",
            model="deepseek-v4-flash",
            prompt_version="reddit-reply-v1",
        )


class _FailingClient:
    async def create_draft(self, request):  # type: ignore[no-untyped-def]
        del request
        raise RuntimeError("provider failure secret-token-123")


@pytest.fixture
async def draft_database(tmp_path: Path) -> Database:
    database = Database(tmp_path / "drafts.sqlite3")
    async with database.connect() as connection:
        await migrate(connection)
    return database


async def _persist_post(database: Database) -> RedditPost:
    async with database.connect() as connection:
        resource = await ResourceRepository(connection).create(
            MonitoredResource(
                id=None,
                original_input="https://www.reddit.com/r/WedditNYC/new/",
                canonical_url="https://www.reddit.com/r/WedditNYC/new/",
                subreddit="WedditNYC",
                resource_type=ResourceType.SUBREDDIT,
                search_query=None,
                sort_mode="new",
            )
        )
        return await PostRepository(connection).create(
            RedditPost(
                id=None,
                reddit_id="p1",
                resource_id=resource.id or 0,
                subreddit="WedditNYC",
                title="Need photographer",
                body="Brooklyn fall wedding, warm tone please.",
                permalink="https://www.reddit.com/r/WedditNYC/comments/p1/post/",
                author="owner",
                created_utc=datetime(2026, 7, 13, 21, 0, tzinfo=UTC).isoformat(),
                matched_keywords_json='["photographer","brooklyn"]',
                status=PostStatus.NEW,
            )
        )


@pytest.mark.asyncio
async def test_draft_persistence_and_status_update(draft_database: Database) -> None:
    post = await _persist_post(draft_database)
    client = _FakeClient()
    service = DraftService(database=draft_database, client=client)

    draft = await service.create_draft(post.id or 0, owner_instruction="Keep it short.")

    assert draft.reddit_post_id == post.id
    assert draft.user_instruction == "Keep it short."
    async with draft_database.connect() as connection:
        saved_post = await PostRepository(connection).get_by_id(post.id or 0)
        drafts = await DraftRepository(connection).list_by_post_id(post.id or 0)
    assert saved_post is not None
    assert saved_post.status == PostStatus.DRAFTED
    assert len(drafts) == 1
    assert drafts[0].draft_text == "Draft reply text"
    assert client.last_request.max_words == 120


@pytest.mark.asyncio
async def test_regenerate_creates_new_draft_record(draft_database: Database) -> None:
    post = await _persist_post(draft_database)
    client = _FakeClient()
    service = DraftService(database=draft_database, client=client)

    first = await service.create_draft(post.id or 0, owner_instruction="version one")
    second = await service.regenerate_draft(post.id or 0)

    assert first.id != second.id
    async with draft_database.connect() as connection:
        drafts = await DraftRepository(connection).list_by_post_id(post.id or 0)
    assert len(drafts) == 2
    assert drafts[-1].user_instruction == "version one"


@pytest.mark.asyncio
async def test_preferences_are_configurable(draft_database: Database) -> None:
    service = DraftService(database=draft_database, client=_FakeClient())

    prefs = await service.update_preferences(
        language="Russian",
        tone="warm and concise",
        max_words=80,
    )
    loaded = await service.get_preferences()

    assert prefs == loaded
    assert loaded.max_words == 80


@pytest.mark.asyncio
async def test_api_failure_is_safe_and_secret_not_logged(
    draft_database: Database,
    caplog: pytest.LogCaptureFixture,
) -> None:
    post = await _persist_post(draft_database)
    service = DraftService(database=draft_database, client=_FailingClient())

    with caplog.at_level(logging.WARNING):
        with pytest.raises(DraftGenerationError):
            await service.create_draft(post.id or 0)

    assert "secret-token-123" not in caplog.text
    assert "RuntimeError" in caplog.text
