from aiogram import Bot, Dispatcher, types

from gino import Gino

from app import config

db = Gino()

bot = Bot(
    token=config.BOT_TOKEN,
    parse_mode=types.ParseMode.HTML,
)

dp = Dispatcher(
    bot=bot,
)

__all__ = (
    "bot",
    "dp",
    "db",
)
