from __future__ import annotations

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from tusya_bot.bot.auth import require_owner
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
    await update.effective_message.reply_text(
        "Monitoring MVP is configured. Live scheduler is not wired yet."
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
