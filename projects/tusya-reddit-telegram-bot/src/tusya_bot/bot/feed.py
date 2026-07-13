from __future__ import annotations

from collections.abc import Awaitable, Callable
from math import ceil

from telegram import CallbackQuery, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from tusya_bot.bot.auth import require_owner
from tusya_bot.bot.callbacks import CallbackPayload, parse_callback
from tusya_bot.delivery.rendering import (
    FEED_PAGE_SIZE,
    build_feed_keyboard,
    build_post_navigation_keyboard,
    chunk_text,
    render_feed_page,
    render_full_post,
)
from tusya_bot.domain.errors import NotFoundError, StaleCallbackError
from tusya_bot.services.post_service import PostService


async def show_feed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    assert update.effective_message is not None
    await _send_feed_page(
        target=update.effective_message.reply_text,
        post_service=context.application.bot_data["post_service"],
        page=0,
    )


async def feed_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer()
    payload = _parse_callback_or_stale(query)
    await _edit_feed_page(
        query=query,
        post_service=context.application.bot_data["post_service"],
        page=payload.page or 0,
    )


async def open_post_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer()
    payload = _parse_callback_or_stale(query)

    post_service: PostService = context.application.bot_data["post_service"]
    try:
        post = await post_service.mark_opened(payload.subject_id)
    except NotFoundError as error:
        raise StaleCallbackError(str(error)) from error

    chunks = chunk_text(render_full_post(post))
    keyboard = build_post_navigation_keyboard(post, page=payload.page)
    await _edit_message_html(query, chunks[0], keyboard)
    for chunk in chunks[1:]:
        await context.bot.send_message(
            chat_id=query.message.chat_id,  # type: ignore[union-attr]
            text=chunk,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )


async def ignore_post_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer("Пост помечен как игнор.")
    payload = _parse_callback_or_stale(query)

    post_service: PostService = context.application.bot_data["post_service"]
    try:
        post = await post_service.mark_ignored(payload.subject_id)
    except NotFoundError as error:
        raise StaleCallbackError(str(error)) from error

    text = chunk_text(render_full_post(post))[0]
    await _edit_message_html(
        query,
        text,
        build_post_navigation_keyboard(post, page=payload.page),
    )


async def draft_placeholder_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer()
    payload = _parse_callback_or_stale(query)
    post_service: PostService = context.application.bot_data["post_service"]
    try:
        post = await post_service.get_post(payload.subject_id)
    except NotFoundError as error:
        raise StaleCallbackError(str(error)) from error

    await context.bot.send_message(
        chat_id=query.message.chat_id,  # type: ignore[union-attr]
        text=(
            "Создание черновика будет добавлено в Phase 4.\n"
            f"Пост сохранен: {post.title}\n"
            "Черновик не опубликован."
        ),
    )


async def noop_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer("Эта кнопка только показывает статус.")


async def stale_callback_error(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    await require_owner(update, context)
    query = update.callback_query
    assert query is not None
    await query.answer("Этот пост больше недоступен.", show_alert=True)


async def _send_feed_page(
    *,
    target: Callable[..., Awaitable[object]],
    post_service: PostService,
    page: int,
) -> None:
    posts, total = await post_service.list_feed_page(page=page, page_size=FEED_PAGE_SIZE)
    total_pages = max(1, ceil(total / FEED_PAGE_SIZE)) if total else 1
    await target(
        render_feed_page(posts, page=page, total_pages=total_pages),
        parse_mode=ParseMode.HTML,
        reply_markup=build_feed_keyboard(posts, page=page, total_pages=total_pages),
        disable_web_page_preview=True,
    )


async def _edit_feed_page(
    *,
    query: CallbackQuery,
    post_service: PostService,
    page: int,
) -> None:
    posts, total = await post_service.list_feed_page(page=page, page_size=FEED_PAGE_SIZE)
    total_pages = max(1, ceil(total / FEED_PAGE_SIZE)) if total else 1
    await _edit_message_html(
        query,
        render_feed_page(posts, page=page, total_pages=total_pages),
        build_feed_keyboard(posts, page=page, total_pages=total_pages),
    )


def _parse_callback_or_stale(query: CallbackQuery) -> CallbackPayload:
    try:
        return parse_callback(query.data or "")
    except (TypeError, ValueError) as error:
        raise StaleCallbackError("Invalid callback payload") from error


async def _edit_message_html(
    query: CallbackQuery,
    text: str,
    reply_markup: InlineKeyboardMarkup,
) -> None:
    if query.message is None:
        raise StaleCallbackError("Callback message is unavailable")
    await query.edit_message_text(
        text=text,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )
