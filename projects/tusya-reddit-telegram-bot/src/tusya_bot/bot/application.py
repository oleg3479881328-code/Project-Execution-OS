from __future__ import annotations

from typing import Any

from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

from tusya_bot.bot.commands import (
    check_now,
    check_now_callback,
    delete_keyword,
    delete_resource,
    list_keywords,
    list_resources,
    menu,
    start,
    status,
    toggle_keyword,
    toggle_resource,
)
from tusya_bot.bot.conversations import build_conversations
from tusya_bot.bot.feed import (
    draft_placeholder_callback,
    feed_callback,
    ignore_post_callback,
    noop_callback,
    open_post_callback,
    show_feed,
)
from tusya_bot.config import Settings
from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.delivery.telegram import TelegramDeliveryService
from tusya_bot.domain.errors import StaleCallbackError, TusyaBotError
from tusya_bot.logging_config import configure_logging
from tusya_bot.monitoring.engine import MonitoringEngine
from tusya_bot.reddit.client import PublicRedditClient
from tusya_bot.services.keyword_service import KeywordService
from tusya_bot.services.post_service import PostService
from tusya_bot.services.resource_service import ResourceService

TelegramApplication = Application[Any, Any, Any, Any, Any, Any]


async def build_application(settings: Settings) -> TelegramApplication:
    settings.prepare_directories()
    configure_logging(settings.log_level)

    database = Database(settings.database_path)
    async with database.connect() as connection:
        await migrate(connection)
    resource_service = ResourceService(database)
    keyword_service = KeywordService(database)
    post_service = PostService(database)
    reddit_client = PublicRedditClient(
        user_agent=settings.reddit_user_agent,
        timeout_seconds=float(settings.reddit_timeout_seconds),
    )

    application = (
        ApplicationBuilder()
        .token(settings.telegram_bot_token.get_secret_value())
        .post_init(_post_init)
        .post_shutdown(_post_shutdown)
        .build()
    )
    delivery_service = TelegramDeliveryService(
        bot=application.bot,
        owner_chat_id=settings.owner_telegram_chat_id,
        post_service=post_service,
    )
    monitoring_engine = MonitoringEngine(
        database=database,
        reddit_client=reddit_client,
        delivery_service=delivery_service,
        poll_interval_seconds=settings.poll_interval_seconds,
    )
    application.bot_data["owner_chat_id"] = settings.owner_telegram_chat_id
    application.bot_data["settings"] = settings
    application.bot_data["database"] = database
    application.bot_data["resource_service"] = resource_service
    application.bot_data["keyword_service"] = keyword_service
    application.bot_data["post_service"] = post_service
    application.bot_data["reddit_client"] = reddit_client
    application.bot_data["delivery_service"] = delivery_service
    application.bot_data["monitoring_engine"] = monitoring_engine

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("check_now", check_now))
    application.add_handler(CommandHandler("feed", show_feed))
    application.add_handler(CommandHandler("resources", list_resources))
    application.add_handler(CommandHandler("keywords", list_keywords))
    application.add_handler(CommandHandler("toggle_resource", toggle_resource))
    application.add_handler(CommandHandler("delete_resource", delete_resource))
    application.add_handler(CommandHandler("toggle_keyword", toggle_keyword))
    application.add_handler(CommandHandler("delete_keyword", delete_keyword))
    application.add_handler(CallbackQueryHandler(check_now_callback, pattern="^check_now$"))
    application.add_handler(CallbackQueryHandler(feed_callback, pattern="^feed:"))
    application.add_handler(CallbackQueryHandler(open_post_callback, pattern="^open:"))
    application.add_handler(CallbackQueryHandler(ignore_post_callback, pattern="^ignore:"))
    application.add_handler(CallbackQueryHandler(draft_placeholder_callback, pattern="^draft:"))
    application.add_handler(CallbackQueryHandler(noop_callback, pattern="^noop:"))
    application.add_handler(MessageHandler(filters.Regex("^📡 Лента$"), show_feed))

    for conversation in build_conversations():
        application.add_handler(conversation)

    application.add_error_handler(_handle_application_error)
    return application


async def _post_init(application: TelegramApplication) -> None:
    monitoring_engine: MonitoringEngine = application.bot_data["monitoring_engine"]
    monitoring_engine.set_monitoring_enabled(application.job_queue is not None)
    if application.job_queue is not None:
        existing = application.job_queue.get_jobs_by_name("tusya-monitoring-cycle")
        if not existing:
            application.job_queue.run_repeating(
                _scheduled_cycle,
                interval=application.bot_data["settings"].poll_interval_seconds,
                first=0,
                name="tusya-monitoring-cycle",
            )


async def _post_shutdown(application: TelegramApplication) -> None:
    reddit_client: PublicRedditClient = application.bot_data["reddit_client"]
    await reddit_client.aclose()


async def _scheduled_cycle(context: CallbackContext[Any, Any, Any, Any]) -> None:
    monitoring_engine: MonitoringEngine = context.application.bot_data["monitoring_engine"]
    await monitoring_engine.run_cycle(trigger="scheduled")


async def _handle_application_error(
    update: object,
    context: CallbackContext[Any, Any, Any, Any],
) -> None:
    error = context.error
    callback_query = getattr(update, "callback_query", None)
    effective_message = getattr(update, "effective_message", None)

    if isinstance(error, StaleCallbackError):
        if callback_query is not None:
            await callback_query.answer("Этот пост больше недоступен.", show_alert=True)
        elif effective_message is not None:
            await effective_message.reply_text("Этот пост больше недоступен.")
        return

    if isinstance(error, TusyaBotError):
        if callback_query is not None:
            await callback_query.answer("Операция сейчас недоступна.", show_alert=True)
        elif effective_message is not None:
            await effective_message.reply_text("Операция сейчас недоступна.")
        return


def _load_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


async def bootstrap_application() -> TelegramApplication:
    settings = _load_settings()
    return await build_application(settings)


def run_bot() -> None:
    import asyncio

    application = asyncio.run(bootstrap_application())
    application.run_polling()
