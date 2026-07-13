from __future__ import annotations

from typing import Any

from telegram.ext import Application, ApplicationBuilder, CommandHandler

from tusya_bot.bot.commands import (
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
from tusya_bot.config import Settings
from tusya_bot.db.engine import Database
from tusya_bot.db.migrations import migrate
from tusya_bot.db.repositories import KeywordRepository, ResourceRepository
from tusya_bot.logging_config import configure_logging
from tusya_bot.services.keyword_service import KeywordService
from tusya_bot.services.resource_service import ResourceService

TelegramApplication = Application[Any, Any, Any, Any, Any, Any]


async def build_application(settings: Settings) -> TelegramApplication:
    settings.prepare_directories()
    configure_logging(settings.log_level)

    database = Database(settings.database_path)
    async with database.connect() as connection:
        await migrate(connection)
        resource_service = ResourceService(ResourceRepository(connection))
        keyword_service = KeywordService(KeywordRepository(connection))

    application = ApplicationBuilder().token(
        settings.telegram_bot_token.get_secret_value()
    ).build()
    application.bot_data["owner_chat_id"] = settings.owner_telegram_chat_id
    application.bot_data["resource_service"] = resource_service
    application.bot_data["keyword_service"] = keyword_service

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("resources", list_resources))
    application.add_handler(CommandHandler("keywords", list_keywords))
    application.add_handler(CommandHandler("toggle_resource", toggle_resource))
    application.add_handler(CommandHandler("delete_resource", delete_resource))
    application.add_handler(CommandHandler("toggle_keyword", toggle_keyword))
    application.add_handler(CommandHandler("delete_keyword", delete_keyword))

    for conversation in build_conversations():
        application.add_handler(conversation)

    return application


def _load_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


async def bootstrap_application() -> TelegramApplication:
    settings = _load_settings()
    return await build_application(settings)


def run_bot() -> None:
    import asyncio

    application = asyncio.run(bootstrap_application())
    application.run_polling()
