from __future__ import annotations

from typing import Any

from telegram import Update
from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from tusya_bot.bot.auth import require_owner
from tusya_bot.bot.feed import _parse_callback_or_stale
from tusya_bot.services.draft_service import DraftService
from tusya_bot.services.keyword_service import KeywordService
from tusya_bot.services.resource_service import ResourceService

ADD_RESOURCE_WAIT_INPUT = 100
ADD_KEYWORD_WAIT_INPUT = 200
REFINE_DRAFT_WAIT_INPUT = 300
DRAFT_SETTINGS_WAIT_INPUT = 400


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


async def refine_draft_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer()
    payload = _parse_callback_or_stale(query)
    if context.user_data is None:
        raise RuntimeError("Conversation user_data is unavailable")
    context.user_data["refine_post_id"] = payload.subject_id
    context.user_data["refine_page"] = payload.page
    await query.message.reply_text(  # type: ignore[union-attr]
        "Пришлите уточнение для черновика. Например: короче, теплее, без упоминания цены."
    )
    return REFINE_DRAFT_WAIT_INPUT


async def refine_draft_save(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    if context.user_data is None:
        raise RuntimeError("Conversation user_data is unavailable")
    post_id = int(context.user_data["refine_post_id"])
    page = context.user_data.get("refine_page")
    service: DraftService = context.application.bot_data["draft_service"]
    draft = await service.refine_draft(post_id, update.effective_message.text or "")
    from tusya_bot.delivery.rendering import build_draft_keyboard, chunk_text, render_draft_text
    chunks = chunk_text(
        render_draft_text(
            draft_text=draft.draft_text,
            provider=draft.provider,
            model=draft.model,
            prompt_version=draft.prompt_version,
            owner_instruction=draft.user_instruction,
        )
    )
    await update.effective_message.reply_text(
        chunks[0],
        parse_mode="HTML",
        reply_markup=build_draft_keyboard(post_id, page=page),
        disable_web_page_preview=True,
    )
    for chunk in chunks[1:]:
        await update.effective_message.reply_text(chunk, parse_mode="HTML")
    context.user_data.pop("refine_post_id", None)
    context.user_data.pop("refine_page", None)
    return ConversationHandler.END


async def draft_settings_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    service: DraftService = context.application.bot_data["draft_service"]
    prefs = await service.get_preferences()
    await update.effective_message.reply_text(
        "Пришлите настройки в формате:\n"
        "language | tone | max_words\n\n"
        f"Сейчас: {prefs.language} | {prefs.tone} | {prefs.max_words}"
    )
    return DRAFT_SETTINGS_WAIT_INPUT


async def draft_settings_save(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await require_owner(update, context)
    assert update.effective_message is not None
    raw = update.effective_message.text or ""
    parts = [part.strip() for part in raw.split("|")]
    if len(parts) != 3:
        await update.effective_message.reply_text(
            "Нужен формат: language | tone | max_words"
        )
        return DRAFT_SETTINGS_WAIT_INPUT
    service: DraftService = context.application.bot_data["draft_service"]
    prefs = await service.update_preferences(
        language=parts[0],
        tone=parts[1],
        max_words=int(parts[2]),
    )
    await update.effective_message.reply_text(
        f"Сохранено: {prefs.language} | {prefs.tone} | {prefs.max_words}"
    )
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
        ConversationHandler(
            entry_points=[CallbackQueryHandler(refine_draft_start, pattern="^refine:")],
            states={
                REFINE_DRAFT_WAIT_INPUT: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, refine_draft_save)
                ]
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        ),
        ConversationHandler(
            entry_points=[CommandHandler("draft_settings", draft_settings_start)],
            states={
                DRAFT_SETTINGS_WAIT_INPUT: [
                    MessageHandler(filters.TEXT & ~filters.COMMAND, draft_settings_save)
                ]
            },
            fallbacks=[CommandHandler("cancel", cancel)],
        ),
    ]
