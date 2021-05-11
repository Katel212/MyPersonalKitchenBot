import datetime as dt
import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.types import Message

from app.keyboards.inline.notice_settings_keyboard import NotificationSettingsListKeyboard
from app.keyboards.inline.notification_frequency_keyboard import NotificationFrequencySettingsKeyboard
from app.keyboards.inline.expiration_date_notifications_keyboard import ExpirationDateNotificationsListKeyboard
from app.keyboards.inline.other_settings_keyboard import OtherSettingsListKeyboard
from app.keyboards.inline.settings_keyboard import SettingsListKeyboard
from app.keyboards.inline.weekly_notification_keyboard import WeeklyNotificationSettings
from app.misc import dp, bot
from app.notification.advance_notifications import advance_notification_checker
from app.notification.frequence_notifications import frequency_notification_checker
from app.notification.weekly_notification import every_day_notification_checker
from app.states.state_freq_number import FreqNumberState
from app.states.state_expiration_date import ExpirationDateState
from app.states.state_day_of_week import DayOfWeekState
from app.models.user_settings import UserSettings


@dp.callback_query_handler(filters.Regexp(r'notification_frequency'))
async def notification_frequency_handler(query: types.CallbackQuery):
    await bot.edit_message_text('Частота уведомлений обо всех продуктах: ', query.message.chat.id, query.message.message_id,
                           reply_markup=NotificationFrequencySettingsKeyboard.create())
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'time_to_expiration_date'))
async def expiration_date_notifications_handler(query: types.CallbackQuery):
    await bot.edit_message_text("Частота уведомлений об истечении срока годности продукта:", query.message.chat.id, query.message.message_id,
                           reply_markup=ExpirationDateNotificationsListKeyboard.create())
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'weekly_notification'))
async def weekly_notification_handler(query: types.CallbackQuery):
    await bot.edit_message_text("Настройка еженедельных уведомлений:", query.message.chat.id, query.message.message_id,
                           reply_markup=WeeklyNotificationSettings.create())
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'disable_notifications_completely'))
async def delete_notification_handler(query: types.CallbackQuery):
    notice = await UserSettings.query.where(UserSettings.user_id == query.from_user.id).gino.first()
    await notice.update(notifications_general_enabled=False).apply()
    await bot.send_message(query.message.chat.id, "Все уведомления отключены")
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'freq_(on|off|number_of_notifications)'))
async def frequency_notification_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'freq_(on|off|number_of_notifications)', query.data).groups()
    source = groups[0]
    freq = await UserSettings.query.where(UserSettings.user_id == query.from_user.id).gino.first()
    if source == 'on':
        await freq.update(notifications_general_enabled=True).apply()
        await freq.update(notifications_periodical_frequency_enabled=True).apply()

        await bot.send_message(query.from_user.id, 'Включено',
                               )
        await freq.update(last_notify_day_frequency=dt.datetime.now()).apply()
        await frequency_notification_checker()

    if source == 'off':
        await freq.update(notifications_periodical_frequency_enabled=False).apply()
        await bot.send_message(query.from_user.id, 'Выключено',
                               )
    if source == 'number_of_notifications':
        await FreqNumberState.number.set()
        await bot.send_message(query.from_user.id, 'Введите переодичность уведомлений:',
                               )
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'date_(on|off|settings)'))
async def frequency_notification_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'date_(on|off|settings)', query.data).groups()
    source = groups[0]
    date = await UserSettings.query.where(UserSettings.user_id == query.from_user.id).gino.first()
    if source == 'on':
        await date.update(notifications_general_enabled=True).apply()
        await date.update(notifications_advance_enabled=True).apply()
        await advance_notification_checker()
        await bot.send_message(query.from_user.id, 'Включено',
                               )
    if source == 'off':
        await date.update(notifications_advance_enabled=False).apply()
        await bot.send_message(query.from_user.id, 'Выключено',
                               )
    if source == 'settings':
        await ExpirationDateState.number.set()
        await bot.send_message(query.from_user.id, 'Введите количество дней до истечения срока годности:',
                               )
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'week_(on|off|day)'))
async def frequency_notification_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'week_(on|off|day)', query.data).groups()
    source = groups[0]
    day = await UserSettings.query.where(UserSettings.user_id == query.from_user.id).gino.first()
    if source == 'on':
        await day.update(notifications_general_enabled=True).apply()
        await day.update(notifications_weekly_enabled=True).apply()
        await bot.send_message(query.from_user.id, 'Включено',
                               )
        await every_day_notification_checker()
    if source == 'off':
        await day.update(notifications_weekly_enabled=False).apply()
        await bot.send_message(query.from_user.id, 'Выключено',
                               )
    if source == 'day':
        await DayOfWeekState.name.set()
        await bot.send_message(query.from_user.id,

                               'Выберете день недели:\n1 - понедельник\n2 - вторник\n3 - среда\n4 - четверг\n5 - пятница\n6 - суббота\n7 - '

                               'воскресенье',
                               )
    await query.answer()


@dp.message_handler(state=FreqNumberState.number)
async def frequency_numbers_per_day_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['number'] = int(msg.text)
            freq = await UserSettings.query.where(UserSettings.user_id == msg.from_user.id).gino.first()
            await freq.update(notifications_general_enabled=True).apply()
            await freq.update(
                notifications_periodical_frequency_enabled=True).apply()
            await freq.update(notifications_periodical_frequency=int(msg.text)).apply()
            await freq.update(last_notify_day_frequency=dt.datetime.now()).apply()
            await frequency_notification_checker()
            await msg.answer('Частота изменена')
            await state.finish()
        else:
            await msg.answer("Некорректный ввод! Введите число")


@dp.message_handler(state=ExpirationDateState.number)
async def expiration_date_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit():
            data['number'] = int(msg.text)
            date = await UserSettings.query.where(UserSettings.user_id == msg.from_user.id).gino.first()
            await date.update(notifications_general_enabled=True).apply()
            await date.update(
                notifications_advance_enabled=True).apply()
            await date.update(notifications_advance_days_until_expiration=int(msg.text)).apply()
            await msg.answer('Количество дней до конца срока годности изменено')
            await advance_notification_checker()
            await state.finish()
        else:
            await msg.answer("Некорректный ввод! Введите число")


@dp.message_handler(state=DayOfWeekState.name)
async def day_of_week_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        if msg.text.isdigit() and int(msg.text) in range(1, 7):
            data['number'] = int(msg.text)
            day = await UserSettings.query.where(UserSettings.user_id == msg.from_user.id).gino.first()
            await day.update(notifications_general_enabled=True).apply()
            await day.update(notifications_weekly_day=int(msg.text)).apply()
            await day.update(
                notifications_weekly_enabled=True).apply()
            await msg.answer('День недели уведомлений изменен')
            await every_day_notification_checker()
            await state.finish()
        else:
            await msg.answer("Некорректный ввод! Введите число")


@dp.callback_query_handler(filters.Regexp(r'back_to_notice_settings'))
async def back_to_notice_settings_handler(query: types.CallbackQuery):
    await bot.edit_message_text("Настройки уведомлений", query.from_user.id, query.message.message_id,reply_markup=NotificationSettingsListKeyboard.create())



@dp.callback_query_handler(filters.Regexp(r'back_to_other_settings'))
async def back_to_other_settings_handler(query: types.CallbackQuery):
    await bot.edit_message_text("Другие настройки:", query.from_user.id, query.message.message_id, reply_markup=OtherSettingsListKeyboard.create())


@dp.callback_query_handler(filters.Regexp(r'back_to_settings'))
async def back_to_settings_handler(query: types.CallbackQuery):
    await bot.edit_message_text("Возможные настройки:", query.from_user.id, query.message.message_id, reply_markup=SettingsListKeyboard.create())
