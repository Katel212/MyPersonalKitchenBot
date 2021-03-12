import datetime
import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.types import Message

from app.keyboards.inline.notification_frequency_keyboard import NotificationFrequencySettingsKeyboard
from app.keyboards.inline.expiration_date_notifications_keyboard import ExpirationDateNotificationsListKeyboard
from app.keyboards.inline.weekly_notification_keyboard import WeeklyNotificationSettings
from app.misc import dp, bot
from app.states.state_freq_number import FreqNumberState
from app.states.state_expiration_date import ExpirationDateState
from app.states.state_day_of_week import DayOfWeekState


@dp.callback_query_handler(filters.Regexp(r'notification_frequency'))
async def notification_frequency_handler(query: types.CallbackQuery):
    await bot.send_message(query.message.chat.id, 'Настройка частоты уведомлений: ',
                           reply_markup=NotificationFrequencySettingsKeyboard.create())


@dp.callback_query_handler(filters.Regexp(r'time_to_expiration_date'))
async def expiration_date_notifications_handler(query: types.CallbackQuery):
    await bot.send_message(query.message.chat.id, "Частота уведомлений о сроке годности :",
                           reply_markup=ExpirationDateNotificationsListKeyboard.create())


@dp.callback_query_handler(filters.Regexp(r'weekly_notification'))
async def weekly_notification_handler(query: types.CallbackQuery):
    await bot.send_message(query.message.chat.id, "Настройка еженедельных уведомлений",
                           reply_markup=WeeklyNotificationSettings.create())


@dp.callback_query_handler(filters.Regexp(r'disable_notifications_completely'))
async def delete_notification_handler(query: types.CallbackQuery):
    await bot.send_message(query.message.chat.id, "Уведомления отключены")


@dp.callback_query_handler(filters.Regexp(r'freq_(on|off|number_of_notifications)'))
async def frequency_notification_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'freq_(on|off|number_of_notifications)', query.data).groups()
    source = groups[0]
    if source == 'on':
        await bot.send_message(query.from_user.id, 'Включить',
                               )
    if source == 'off':
        await bot.send_message(query.from_user.id, 'Выключить',
                               )
    if source == 'number_of_notifications':
        await FreqNumberState.number.set()
        await bot.send_message(query.from_user.id, 'Введите колиство уведомлений',
                               )


@dp.callback_query_handler(filters.Regexp(r'date_(on|off|settings)'))
async def frequency_notification_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'date_(on|off|settings)', query.data).groups()
    source = groups[0]
    if source == 'on':
        await bot.send_message(query.from_user.id, 'Включить',
                               )
    if source == 'off':
        await bot.send_message(query.from_user.id, 'Выключить',
                               )
    if source == 'settings':
        await ExpirationDateState.number.set()
        await bot.send_message(query.from_user.id, 'Введите количество дней до истечения срока годности',
                               )


@dp.callback_query_handler(filters.Regexp(r'week_(on|off|day)'))
async def frequency_notification_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'week_(on|off|day)', query.data).groups()
    source = groups[0]
    if source == 'on':
        await bot.send_message(query.from_user.id, 'Включить',
                               )
    if source == 'off':
        await bot.send_message(query.from_user.id, 'Выключить',
                               )
    if source == 'day':
        await DayOfWeekState.name.set()
        await bot.send_message(query.from_user.id, 'Введите количество дней до истечения срока годности',
                               )


@dp.message_handler(state=FreqNumberState.number)
async def frequency_numbers_per_day_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = int(msg.text)
        await msg.answer('Частота изменена')

    await state.finish()


@dp.message_handler(state=ExpirationDateState.number)
async def expiration_date_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = int(msg.text)
        await msg.answer('Время до конца срока годности изменено')
    await state.finish()

@dp.message_handler(state=DayOfWeekState.name)
async def frequency_numbers_per_day_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
        await msg.answer('День недели измененён')
    await state.finish()