import re

from aiogram import types

from aiogram.dispatcher import filters

from app.misc import dp, bot

from app.keyboards.inline.notice_settings_keyboard import NotificationSettingsListKeyboard
from app.keyboards.inline.other_settings_keyboard import OtherSettingsListKeyboard


@dp.callback_query_handler(filters.Regexp(r'settings_(other|notification_settings)'))
async def notification_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'settings_(other|notification_settings)', query.data).groups()
    source = groups[0]
    if source == 'notification_settings':
        await bot.send_message(query.from_user.id, 'Настройки уведомлений:',
                               reply_markup=NotificationSettingsListKeyboard.create())
    elif source == 'other':
        await bot.send_message(query.from_user.id, 'Другие настройки:',
                               reply_markup=OtherSettingsListKeyboard.create())
