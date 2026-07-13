from __future__ import annotations

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes

from tusya_bot.bot.auth import require_owner
from tusya_bot.monitoring.engine import MonitoringEngine
from tusya_bot.monitoring.models import MonitoringStatusSnapshot
from tusya_bot.services.keyword_service import KeywordService
from tusya_bot.services.resource_service import ResourceService

MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["📡 Лента", "➕ Добавить ресурс"],
        ["🔤 Добавить слово", "🗂 Ресурсы"],
        ["🧾 Слова", "⚙️ Настройки"],
    ],
    resize_keyboard=True,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    await update.effective_message.reply_text("Туся готова к работе.", reply_markup=MAIN_MENU)


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    await update.effective_message.reply_text("Главное меню.", reply_markup=MAIN_MENU)


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    snapshot = await monitoring_engine.get_status_snapshot()
    await update.effective_message.reply_text(
        _render_status_text(snapshot),
        reply_markup=_status_keyboard(),
    )


async def check_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    result = await monitoring_engine.run_cycle(trigger="manual")
    await update.effective_message.reply_text(_render_check_now_result(result.emitted_candidates))


async def check_now_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    query = update.callback_query
    chat = update.effective_chat
    assert query is not None
    assert chat is not None
    await query.answer()

    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    result = await monitoring_engine.run_cycle(trigger="manual")
    await context.bot.send_message(
        chat_id=chat.id,
        text=_render_check_now_result(result.emitted_candidates),
    )


async def list_resources(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    service: ResourceService = context.application.bot_data["resource_service"]
    resources = await service.list_resources()
    if not resources:
        await update.effective_message.reply_text("Ресурсов пока нет.")
        return
    lines = [
        (
            f"{resource.id}. [{'on' if resource.enabled else 'off'}] "
            f"r/{resource.subreddit} -> {resource.canonical_url}"
        )
        for resource in resources
    ]
    await update.effective_message.reply_text("\n".join(lines))


async def list_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    service: KeywordService = context.application.bot_data["keyword_service"]
    keywords = await service.list_keywords()
    if not keywords:
        await update.effective_message.reply_text("Слов пока нет.")
        return
    lines = [
        (
            f"{keyword.id}. [{'on' if keyword.enabled else 'off'}] "
            f"{keyword.keyword} [{keyword.match_mode.value}]"
        )
        for keyword in keywords
    ]
    await update.effective_message.reply_text("\n".join(lines))


async def toggle_resource(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    args = context.args or []
    if len(args) != 2:
        await update.effective_message.reply_text("Usage: /toggle_resource <id> <on|off>")
        return
    resource_id = int(args[0])
    enabled = args[1].lower() == "on"
    service: ResourceService = context.application.bot_data["resource_service"]
    await service.toggle_resource(resource_id, enabled)
    await update.effective_message.reply_text("Настройка ресурса обновлена.")


async def delete_resource(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    args = context.args or []
    if len(args) != 1:
        await update.effective_message.reply_text("Usage: /delete_resource <id>")
        return
    service: ResourceService = context.application.bot_data["resource_service"]
    await service.delete_resource(int(args[0]))
    await update.effective_message.reply_text("Ресурс удален.")


async def toggle_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    args = context.args or []
    if len(args) != 2:
        await update.effective_message.reply_text("Usage: /toggle_keyword <id> <on|off>")
        return
    keyword_id = int(args[0])
    enabled = args[1].lower() == "on"
    service: KeywordService = context.application.bot_data["keyword_service"]
    await service.toggle_keyword(keyword_id, enabled)
    await update.effective_message.reply_text("Настройка слова обновлена.")


async def delete_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    args = context.args or []
    if len(args) != 1:
        await update.effective_message.reply_text("Usage: /delete_keyword <id>")
        return
    service: KeywordService = context.application.bot_data["keyword_service"]
    await service.delete_keyword(int(args[0]))
    await update.effective_message.reply_text("Слово удалено.")


def _status_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("Check now", callback_data="check_now")]]
    )


def _render_status_text(snapshot: MonitoringStatusSnapshot) -> str:
    monitoring_state = "on" if snapshot.monitoring_enabled else "off"
    return "\n".join(
        [
            f"Monitoring: {monitoring_state}",
            f"Resources: {snapshot.resource_count}",
            f"Keywords: {snapshot.keyword_count}",
            f"Running now: {'yes' if snapshot.running else 'no'}",
            f"Last cycle start: {snapshot.last_cycle_started_at or '-'}",
            f"Last cycle finish: {snapshot.last_cycle_finished_at or '-'}",
            f"Last error: {snapshot.last_cycle_error or '-'}",
            f"Next cycle: {snapshot.next_cycle_at or '-'}",
        ]
    )


def _render_check_now_result(emitted_candidates: int) -> str:
    return f"Check now completed. New matching candidates: {emitted_candidates}."
