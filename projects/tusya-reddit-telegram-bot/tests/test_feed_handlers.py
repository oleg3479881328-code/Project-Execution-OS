from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest
from telegram import InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from tusya_bot.bot.application import _post_init
from tusya_bot.bot.callbacks import encode_callback
from tusya_bot.bot.feed import (
    draft_create_callback,
    feed_callback,
    ignore_post_callback,
    open_post_callback,
    redraft_callback,
    show_feed,
)
from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.db.repositories import PostRepository, ResourceRepository
from tusya_bot.domain.enums import PostStatus, ResourceType
from tusya_bot.domain.errors import StaleCallbackError, UnauthorizedChatError
from tusya_bot.domain.models import MonitoredResource, RedditPost
from tusya_bot.services.post_service import PostService


class _FakeMessage:
    def __init__(self, *, chat_id: int = 123) -> None:
        self.chat_id = chat_id
        self.calls: list[dict[str, object]] = []

    async def reply_text(self, text: str, **kwargs: object) -> None:
        self.calls.append({"text": text, **kwargs})


class _FakeQuery:
    def __init__(self, data: str, *, chat_id: int = 123) -> None:
        self.data = data
        self.message = _FakeMessage(chat_id=chat_id)
        self.answers: list[tuple[str | None, bool]] = []
        self.edits: list[dict[str, object]] = []

    async def answer(self, text: str | None = None, show_alert: bool = False) -> None:
        self.answers.append((text, show_alert))

    async def edit_message_text(self, text: str, **kwargs: object) -> None:
        self.edits.append({"text": text, **kwargs})


class _FakeBot:
    def __init__(self) -> None:
        self.sent: list[dict[str, object]] = []

    async def send_message(self, **kwargs: object) -> None:
        self.sent.append(kwargs)


class _FakeDraftService:
    async def create_draft(self, post_id: int):  # type: ignore[no-untyped-def]
        return SimpleNamespace(
            reddit_post_id=post_id,
            draft_text="Draft reply",
            provider="deepseek",
            model="deepseek-v4-flash",
            prompt_version="reddit-reply-v1",
            user_instruction=None,
        )

    async def regenerate_draft(self, post_id: int):  # type: ignore[no-untyped-def]
        return await self.create_draft(post_id)


class _FakeJobQueue:
    def __init__(self) -> None:
        self.jobs: list[tuple[str, object, int, int]] = []

    def get_jobs_by_name(self, name: str) -> list[tuple[str, object, int, int]]:
        return [job for job in self.jobs if job[0] == name]

    def run_repeating(
        self,
        callback: object,
        *,
        interval: int,
        first: int,
        name: str,
    ) -> None:
        self.jobs.append((name, callback, interval, first))


class _FakeMonitoringEngine:
    def __init__(self) -> None:
        self.enabled = True

    async def initialize_runtime_state(self) -> None:
        return None

    def set_monitoring_enabled(self, enabled: bool) -> None:
        self.enabled = enabled


@pytest.fixture
async def feed_database(tmp_path: Path) -> Database:
    database = Database(tmp_path / "feed.sqlite3")
    async with database.connect() as connection:
        await migrate(connection)
    return database


async def _persist_posts(database: Database, count: int) -> list[RedditPost]:
    posts: list[RedditPost] = []
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
        repo = PostRepository(connection)
        for index in range(count):
            posts.append(
                await repo.create(
                    RedditPost(
                        id=None,
                        reddit_id=f"id-{index}",
                        resource_id=resource.id or 0,
                        subreddit="WedditNYC",
                        title=f"Post {index}",
                        body="Body " * 800 if index == 0 else "Short body",
                        permalink=f"https://reddit.example/{index}",
                        author="tester",
                        created_utc=datetime(
                            2026, 7, 13, 21, index, tzinfo=UTC
                        ).isoformat(),
                        matched_keywords_json='["photo"]',
                        status=PostStatus.NEW,
                    )
                )
            )
    return posts


def _context(
    *,
    database: Database,
    owner_chat_id: int = 123,
    bot: _FakeBot | None = None,
) -> SimpleNamespace:
    return SimpleNamespace(
        application=SimpleNamespace(
            bot_data={
                "owner_chat_id": owner_chat_id,
                "post_service": PostService(database),
                "draft_service": _FakeDraftService(),
                "settings": SimpleNamespace(poll_interval_seconds=300),
            }
        ),
        bot=bot or _FakeBot(),
    )


@pytest.mark.asyncio
async def test_open_in_bot_flow_and_long_post_chunking(feed_database: Database) -> None:
    posts = await _persist_posts(feed_database, 1)
    query = _FakeQuery(encode_callback("open", posts[0].id or 0, page=0))
    bot = _FakeBot()
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=_FakeMessage(),
        callback_query=query,
    )

    await open_post_callback(
        cast(Update, update),
        cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database, bot=bot)),
    )

    assert query.edits
    assert "Post 0" in str(query.edits[0]["text"])
    assert bot.sent
    async with feed_database.connect() as connection:
        saved = await PostRepository(connection).get_by_id(posts[0].id or 0)
    assert saved is not None
    assert saved.status == PostStatus.OPENED


@pytest.mark.asyncio
async def test_ignore_transition(feed_database: Database) -> None:
    posts = await _persist_posts(feed_database, 1)
    query = _FakeQuery(encode_callback("ignore", posts[0].id or 0, page=0))
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=_FakeMessage(),
        callback_query=query,
    )

    await ignore_post_callback(
        cast(Update, update),
        cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database)),
    )

    assert query.answers == [("Пост помечен как игнор.", False)]
    async with feed_database.connect() as connection:
        saved = await PostRepository(connection).get_by_id(posts[0].id or 0)
    assert saved is not None
    assert saved.status == PostStatus.IGNORED


@pytest.mark.asyncio
async def test_feed_pagination(feed_database: Database) -> None:
    await _persist_posts(feed_database, 7)
    message = _FakeMessage()
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=message,
    )

    await show_feed(
        cast(Update, update),
        cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database)),
    )

    assert message.calls
    keyboard = cast(InlineKeyboardMarkup, message.calls[0]["reply_markup"])
    assert keyboard is not None
    labels = [button.text for row in keyboard.inline_keyboard for button in row]
    assert "→" in labels

    query = _FakeQuery(encode_callback("feed", 0, page=1))
    callback_update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=_FakeMessage(),
        callback_query=query,
    )
    await feed_callback(
        cast(Update, callback_update),
        cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database)),
    )
    assert query.edits
    assert "страница 2/2" in str(query.edits[0]["text"])


@pytest.mark.asyncio
async def test_stale_deleted_callback(feed_database: Database) -> None:
    query = _FakeQuery(encode_callback("open", 999, page=0))
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=_FakeMessage(),
        callback_query=query,
    )

    with pytest.raises(StaleCallbackError):
        await open_post_callback(
            cast(Update, update),
            cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database)),
        )


@pytest.mark.asyncio
async def test_draft_create_and_regenerate_callbacks(feed_database: Database) -> None:
    posts = await _persist_posts(feed_database, 1)
    bot = _FakeBot()

    create_update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=_FakeMessage(),
        callback_query=_FakeQuery(encode_callback("draft", posts[0].id or 0, page=0)),
    )
    await draft_create_callback(
        cast(Update, create_update),
        cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database, bot=bot)),
    )
    assert bot.sent
    assert "Черновик ответа" in str(bot.sent[0]["text"])

    bot.sent.clear()
    regenerate_update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=_FakeMessage(),
        callback_query=_FakeQuery(encode_callback("redraft", posts[0].id or 0, page=0)),
    )
    await redraft_callback(
        cast(Update, regenerate_update),
        cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database, bot=bot)),
    )
    assert bot.sent
    assert "Черновик ответа" in str(bot.sent[0]["text"])


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "handler,update_factory",
    [
        (
            show_feed,
            lambda: SimpleNamespace(
                effective_chat=SimpleNamespace(id=999),
                effective_message=_FakeMessage(),
            ),
        ),
        (
            open_post_callback,
            lambda: SimpleNamespace(
                effective_chat=SimpleNamespace(id=999),
                effective_message=_FakeMessage(),
                callback_query=_FakeQuery(encode_callback("open", 1, page=0)),
            ),
        ),
        (
            ignore_post_callback,
            lambda: SimpleNamespace(
                effective_chat=SimpleNamespace(id=999),
                effective_message=_FakeMessage(),
                callback_query=_FakeQuery(encode_callback("ignore", 1, page=0)),
            ),
        ),
        (
            draft_create_callback,
            lambda: SimpleNamespace(
                effective_chat=SimpleNamespace(id=999),
                effective_message=_FakeMessage(),
                callback_query=_FakeQuery(encode_callback("draft", 1, page=0)),
            ),
        ),
        (
            redraft_callback,
            lambda: SimpleNamespace(
                effective_chat=SimpleNamespace(id=999),
                effective_message=_FakeMessage(),
                callback_query=_FakeQuery(encode_callback("redraft", 1, page=0)),
            ),
        ),
    ],
)
async def test_owner_only_authorization_for_new_handlers(
    feed_database: Database,
    handler: Any,
    update_factory: Any,
) -> None:
    update = update_factory()

    with pytest.raises(UnauthorizedChatError):
        await handler(
            cast(Update, update),
            cast(ContextTypes.DEFAULT_TYPE, _context(database=feed_database, owner_chat_id=123)),
        )


@pytest.mark.asyncio
async def test_application_wiring_does_not_start_duplicate_schedulers() -> None:
    job_queue = _FakeJobQueue()
    application = SimpleNamespace(
        bot_data={
            "monitoring_engine": _FakeMonitoringEngine(),
            "settings": SimpleNamespace(poll_interval_seconds=300),
        },
        job_queue=job_queue,
    )

    await _post_init(application)  # type: ignore[arg-type]
    await _post_init(application)  # type: ignore[arg-type]

    assert len(job_queue.jobs) == 1
