import logging

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat

from src.app.core.config import Settings

logger = logging.getLogger(__name__)


async def bot_commands(bot: Bot, settings: Settings):
    # User commands
    user_commands = [
        BotCommand(command="start", description="Restart"),
        BotCommand(command="top", description="Top Popular Songs"),
        BotCommand(command="lang", description="Choose a language"),
        BotCommand(command="media_effect", description="Media effect"),
        BotCommand(command="about", description="About"),
    ]

    # Set global commands (all users)
    await bot.set_my_commands(commands=user_commands)

    # Admin commands (same + extra)
    admin_commands = user_commands + [
        BotCommand(command="admin_menu", description="Admin main menu")
    ]

    # Set admin-specific commands
    for admin_id in settings.admins_ids:
        try:
            chat_id = int(admin_id)

            scope = BotCommandScopeChat(chat_id=chat_id)
            await bot.set_my_commands(
                commands=admin_commands,
                scope=scope
            )

        except Exception as e:
            logger.warning(
                f"Could not set admin commands for chat {admin_id}: {e}"
            )
