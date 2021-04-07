import schedule
import time
import datetime as dt

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sqlalchemy import and_

from app.models import UserSettings
from app.models.product import Product
from app.misc import dp, bot


async def every_day_notification_checker():
    day = dt.datetime.now().weekday()
    users = await UserSettings.query.where(and_(
        UserSettings.notifications_general_enabled, UserSettings.notifications_weekly_enabled,
        UserSettings.notifications_weekly_day == day)
    ).gino.all()
    for u in users:
        answer = "Истекает срок годности :\n"
        p = await Product.query.where(and_(Product.user_id == u.user_id,
                                           Product.expiration_date <= dt.datetime.now())).gino.all()
        for pr in p:
            answer += pr.name + " " + str(pr.expiration_date) + "\n"
        await bot.send_message(u.user_id, answer)


scheduler = AsyncIOScheduler()
scheduler.add_job(every_day_notification_checker(), trigger=IntervalTrigger(days=7))
scheduler.start()
