from __future__ import annotations

from types import SimpleNamespace
from typing import cast

import pytest
from telegram import Update
from telegram.ext import ContextTypes

from tusya_bot.bot.commands import check_now_callback, status
from tusya_bot.domain.errors import UnauthorizedChatError
from tusya_bot.monitoring.models import CycleResult, MonitoringStatusSnapshot


class _FakeMessage:
    def __init__(self) -> None:
        self.calls: list[tuple[str, object | None]] = []

    async def reply_text(self, text: str, reply_markup: object | None = None) -> None:
        self.calls.append((text, reply_markup))


class _FakeQuery:
    def __init__(self) -> None:
        self.answered = False

    async def answer(self) -> None:
        self.answered = True


class _FakeBot:
    def __init__(self) -> None:
        self.sent: list[tuple[int, str]] = []

    async def send_message(self, *, chat_id: int, text: str) -> None:
        self.sent.append((chat_id, text))


class _FakeEngine:
    async def get_status_snapshot(self) -> MonitoringStatusSnapshot:
        return MonitoringStatusSnapshot(
            monitoring_enabled=True,
            running=False,
            resource_count=2,
            keyword_count=3,
            last_cycle_started_at="2026-07-13T20:00:00+00:00",
            last_cycle_finished_at="2026-07-13T20:01:00+00:00",
            last_cycle_error=None,
            next_cycle_at="2026-07-13T20:06:00+00:00",
        )

    async def run_cycle(self, *, trigger: str) -> CycleResult:
        return CycleResult(
            trigger=trigger,
            overlap_skipped=False,
            processed_resources=1,
            emitted_candidates=2,
            failed_resources=0,
        )


def _context(*, owner_chat_id: int) -> SimpleNamespace:
    return SimpleNamespace(
        application=SimpleNamespace(
            bot_data={
                "owner_chat_id": owner_chat_id,
                "monitoring_engine": _FakeEngine(),
            }
        ),
        bot=_FakeBot(),
    )


@pytest.mark.asyncio
async def test_status_owner_authorization() -> None:
    message = _FakeMessage()
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=999),
        effective_message=message,
    )

    with pytest.raises(UnauthorizedChatError):
        await status(
            cast(Update, update),
            cast(ContextTypes.DEFAULT_TYPE, _context(owner_chat_id=123)),
        )

    assert message.calls == [("Access denied.", None)]


@pytest.mark.asyncio
async def test_check_now_owner_authorization() -> None:
    message = _FakeMessage()
    query = _FakeQuery()
    update = SimpleNamespace(
        effective_chat=SimpleNamespace(id=999),
        effective_message=message,
        callback_query=query,
    )

    with pytest.raises(UnauthorizedChatError):
        await check_now_callback(
            cast(Update, update),
            cast(ContextTypes.DEFAULT_TYPE, _context(owner_chat_id=123)),
        )

    assert message.calls == [("Access denied.", None)]
