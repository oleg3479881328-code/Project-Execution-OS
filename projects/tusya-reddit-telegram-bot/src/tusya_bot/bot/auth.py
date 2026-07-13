from __future__ import annotations

from telegram import Update
from telegram.ext import ContextTypes

from tusya_bot.domain.errors import UnauthorizedChatError


async def require_owner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    chat = update.effective_chat
    owner_chat_id = context.application.bot_data["owner_chat_id"]
    if chat is None or chat.id != owner_chat_id:
        if update.effective_message is not None:
            await update.effective_message.reply_text("Access denied.")
        raise UnauthorizedChatError("Unauthorized Telegram chat")
    return True
