from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from types import SimpleNamespace
from typing import cast

import pytest
from pydantic import SecretStr
from telegram import Update
from telegram.ext import ContextTypes

from tusya_bot.bot.commands import help_command, monitoring_off, monitoring_on
from tusya_bot.config import Settings
from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.monitoring.engine import MonitoringEngine


class _FakeMessage:
    def __init__(self) -> None:
        self.calls: list[str] = []

    async def reply_text(self, text: str, **kwargs: object) -> None:
        del kwargs
        self.calls.append(text)


class _FakeRedditClient:
    async def fetch_posts(self, resource, *, limit: int = 25):  # type: ignore[no-untyped-def]
        del resource, limit
        return []


async def _engine(database: Database) -> MonitoringEngine:
    return MonitoringEngine(
        database=database,
        reddit_client=_FakeRedditClient(),
        delivery_service=SimpleNamespace(deliver_candidates=lambda candidates: None),
        poll_interval_seconds=300,
    )


@pytest.fixture
async def ops_database(tmp_path: Path) -> Database:
    database = Database(tmp_path / "ops.sqlite3")
    async with database.connect() as connection:
        await migrate(connection)
    return database


@pytest.mark.asyncio
async def test_help_command_russian_owner_flow() -> None:
    message = _FakeMessage()
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=message,
    )
    context = SimpleNamespace(application=SimpleNamespace(bot_data={"owner_chat_id": 123}))

    await help_command(
        cast(Update, update),
        cast(ContextTypes.DEFAULT_TYPE, context),
    )

    assert message.calls
    assert "Как работать с Тусей" in message.calls[0]
    assert "/draft_settings" in message.calls[0]


@pytest.mark.asyncio
async def test_monitoring_toggle_persists(ops_database: Database) -> None:
    engine = await _engine(ops_database)
    await engine.initialize_runtime_state()
    message = _FakeMessage()
    context = SimpleNamespace(
        application=SimpleNamespace(
            bot_data={
                "owner_chat_id": 123,
                "monitoring_engine": engine,
            }
        )
    )
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=123),
        effective_message=message,
    )

    await monitoring_off(cast(Update, update), cast(ContextTypes.DEFAULT_TYPE, context))
    snapshot = await engine.get_status_snapshot()
    assert snapshot.monitoring_enabled is False

    restarted = await _engine(ops_database)
    await restarted.initialize_runtime_state()
    restarted_snapshot = await restarted.get_status_snapshot()
    assert restarted_snapshot.monitoring_enabled is False

    await monitoring_on(cast(Update, update), cast(ContextTypes.DEFAULT_TYPE, context))
    enabled_snapshot = await engine.get_status_snapshot()
    assert enabled_snapshot.monitoring_enabled is True


def test_settings_runtime_diagnostics_do_not_expose_secrets(tmp_path: Path) -> None:
    settings = Settings(
        telegram_bot_token=SecretStr("123456:abcde-token"),
        owner_telegram_chat_id=123,
        deepseek_api_key=SecretStr("deepseek-key-12345"),
        database_path=tmp_path / "data" / "tusya.sqlite3",
    )

    diagnostics = settings.runtime_diagnostics()
    rendered = json.dumps(diagnostics)

    assert "deepseek-key-12345" not in rendered
    assert "123456:abcde-token" not in rendered
    assert diagnostics["owner_telegram_chat_id"] == 123


def test_healthcheck_verifies_wal(tmp_path: Path) -> None:
    database_path = tmp_path / "health.sqlite3"

    from tusya_bot.__main__ import run_healthcheck

    run_healthcheck(database_path)

    connection = sqlite3.connect(database_path)
    try:
        cursor = connection.execute("PRAGMA journal_mode;")
        assert str(cursor.fetchone()[0]).lower() == "wal"
    finally:
        connection.close()
