from __future__ import annotations

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes

from tusya_bot.bot.auth import require_owner
from tusya_bot.delivery.protocols import DeliveryService
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


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    await update.effective_message.reply_text(
        "\n".join(
            [
                "Как работать с Тусей:",
                "1. Добавьте ресурс: /add_resource",
                "2. Добавьте ключевое слово: /add_keyword",
                "3. Проверьте статус: /status",
                "4. Запустите ручную проверку: /check_now",
                "5. Откройте ленту: /feed",
                "6. Настройте черновики: /draft_settings",
                "7. Приостановить мониторинг: /monitoring_off",
                "8. Возобновить мониторинг: /monitoring_on",
            ]
        ),
        reply_markup=MAIN_MENU,
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    snapshot = await monitoring_engine.get_status_snapshot()
    await update.effective_message.reply_text(
        _render_status_text(snapshot),
        reply_markup=_status_keyboard(),
    )


async def monitoring_on(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    await monitoring_engine.persist_monitoring_enabled(True)
    await update.effective_message.reply_text("Мониторинг включен.")


async def monitoring_off(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    await monitoring_engine.persist_monitoring_enabled(False)
    await update.effective_message.reply_text("Мониторинг выключен.")


async def check_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    delivery_service: DeliveryService = context.application.bot_data["delivery_service"]
    result = await monitoring_engine.run_cycle(trigger="manual")
    failures = getattr(delivery_service, "last_batch_failures", 0)
    await update.effective_message.reply_text(
        _render_check_now_result(result.emitted_candidates, failures=failures)
    )


async def check_now_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    query = update.callback_query
    chat = update.effective_chat
    assert query is not None
    assert chat is not None
    await query.answer()

    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    delivery_service: DeliveryService = context.application.bot_data["delivery_service"]
    result = await monitoring_engine.run_cycle(trigger="manual")
    failures = getattr(delivery_service, "last_batch_failures", 0)
    await context.bot.send_message(
        chat_id=chat.id,
        text=_render_check_now_result(result.emitted_candidates, failures=failures),
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
        await update.effective_message.reply_text(
            "Формат: /toggle_resource <id> <on|off>"
        )
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
        await update.effective_message.reply_text("Формат: /delete_resource <id>")
        return
    service: ResourceService = context.application.bot_data["resource_service"]
    await service.delete_resource(int(args[0]))
    await update.effective_message.reply_text("Ресурс удален.")


async def toggle_keyword(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    args = context.args or []
    if len(args) != 2:
        await update.effective_message.reply_text(
            "Формат: /toggle_keyword <id> <on|off>"
        )
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
        await update.effective_message.reply_text("Формат: /delete_keyword <id>")
        return
    service: KeywordService = context.application.bot_data["keyword_service"]
    await service.delete_keyword(int(args[0]))
    await update.effective_message.reply_text("Слово удалено.")


def _status_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("Проверить сейчас", callback_data="check_now")]]
    )


def _render_status_text(snapshot: MonitoringStatusSnapshot) -> str:
    monitoring_state = "включен" if snapshot.monitoring_enabled else "выключен"
    return "\n".join(
        [
            f"Мониторинг: {monitoring_state}",
            f"Ресурсы: {snapshot.resource_count}",
            f"Ключевые слова: {snapshot.keyword_count}",
            f"Цикл выполняется: {'да' if snapshot.running else 'нет'}",
            f"Последний старт цикла: {snapshot.last_cycle_started_at or '-'}",
            f"Последнее завершение цикла: {snapshot.last_cycle_finished_at or '-'}",
            f"Последняя ошибка: {snapshot.last_cycle_error or '-'}",
            f"Следующий цикл: {snapshot.next_cycle_at or '-'}",
        ]
    )


def _render_check_now_result(emitted_candidates: int, *, failures: int = 0) -> str:
    base = f"Ручная проверка завершена. Новых подходящих постов: {emitted_candidates}."
    if failures:
        return f"{base}\nЧасть Telegram-доставок завершилась с ошибкой."
    return base
