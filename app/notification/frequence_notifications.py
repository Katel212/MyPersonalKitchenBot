import datetime as dt
from typing import List

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dateutil.parser import parse
from sqlalchemy import and_

from app.misc import bot
from app.models import UserSettings
from app.models.product import Product


async def frequency_notification_checker():
    user_settings: List[UserSettings] = await UserSettings.query.where(and_(
        UserSettings.notifications_general_enabled, UserSettings.notifications_periodical_frequency_enabled)
    ).gino.all()
    for settings in user_settings:
        if settings.last_notify_day_frequency <= (dt.datetime.now() - dt.timedelta(settings.notifications_periodical_frequency)).date():
            answer = "Истекает срок годности:\n"
            p = await Product.query.where(and_(Product.user_id == settings.user_id,
                                               Product.expiration_date <= dt.datetime.today() + dt.timedelta(7))).gino.all()
            for pr in p:
                answer += pr.name + " - " + parse(str(pr.expiration_date)).strftime('%d.%m') + "\n"
            await bot.send_message(settings.user_id, answer)
            UserSettings.last_notify_day_frequency = dt.datetime.now().date()


scheduler = AsyncIOScheduler()
scheduler.add_job(frequency_notification_checker, 'cron', hour='18', minute='00')
scheduler.start()
