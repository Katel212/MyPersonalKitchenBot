from aiogram import Dispatcher
from aiogram import Dispatcher
from aiogram.utils import executor

from app import utils, config
from app.misc import dp
from app.models import base


# from app.notifications.weekly_notifications import weekly_notifications
# The configuration of the modules using import

async def on_startup(dispatcher: Dispatcher):
    await utils.setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    await base.connect(config.POSTGRES_URI)
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins(config.ADMINS_ID)
    # await weekly_notifications(280536886)
    # schedule.run_all()


async def on_shutdown(dispatcher: Dispatcher):
    await base.close_connection()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=config.SKIP_UPDATES)
