from __future__ import annotations

from typing import Any

from telegram import Update
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from tusya_bot.bot.auth import require_owner
from tusya_bot.services.keyword_service import KeywordService
from tusya_bot.services.resource_service import ResourceService

ADD_RESOURCE_WAIT_INPUT = 100
ADD_KEYWORD_WAIT_INPUT = 200


async def add_resource_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    await update.effective_message.reply_text("Пришлите Reddit URL или r/subreddit.")
    return ADD_RESOURCE_WAIT_INPUT


async def add_resource_save(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    service: ResourceService = context.application.bot_data["resource_service"]
    resource = await service.add_resource(update.effective_message.text or "")
    await update.effective_message.reply_text(f"Сохранено: {resource.canonical_url}")
    return ConversationHandler.END


async def add_keyword_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    await update.effective_message.reply_text("Пришлите слово или фразу для мониторинга.")
    return ADD_KEYWORD_WAIT_INPUT


async def add_keyword_save(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    service: KeywordService = context.application.bot_data["keyword_service"]
    keyword = await service.add_keyword(update.effective_message.text or "")
    await update.effective_message.reply_text(f"Сохранено слово: {keyword.keyword}")
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    await update.effective_message.reply_text("Действие отменено.")
    return ConversationHandler.END


def build_conversations() -> list[ConversationHandler[Any]]:
    return [
        ConversationHandler(
            entry_points=[CommandHandler("add_resource", add_resource_start)],
            states={
                ADD_RESOURCE_WAIT_INPUT: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, add_resource_save)
                ]
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        ),
        ConversationHandler(
            entry_points=[CommandHandler("add_keyword", add_keyword_start)],
            states={
                ADD_KEYWORD_WAIT_INPUT: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, add_keyword_save)
                ]
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        ),
    ]
