import re

from aiogram import types

from aiogram.dispatcher import filters

from app.misc import dp, bot

from app.keyboards.inline.automatic_setting_of_the_purchase_date_keyboard import \
    AutomaticSettingOfThePurchaseDateListKeyboard
from app.keyboards.inline.default_list_of_products_keyboard import DefaultListOfProductsListKeyboard


@dp.callback_query_handler(filters.Regexp(r'other_(default_list_of_products|auto_set_purchase_date)'))
async def other_settings_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'other_(default_list_of_products|auto_set_purchase_date)', query.data).groups()
    source = groups[0]
    if source == 'auto_set_purchase_date':
        await bot.send_message(query.from_user.id, 'Настройка автоматической выставления даты:',
                               reply_markup=AutomaticSettingOfThePurchaseDateListKeyboard.create())
    elif source == 'default_list_of_products':
        await bot.send_message(query.from_user.id, 'Настройка дефолтного списка покупок:',
                               reply_markup=DefaultListOfProductsListKeyboard.create())


@dp.callback_query_handler(filters.Regexp(r'purchase_date_list_(on|off)'))
async def purchase_date_list_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'purchase_date_list_(on|off)', query.data).groups()
    source = groups[0]
    if source == 'on':
        await bot.send_message(query.from_user.id, 'Включено',
                               )
    elif source == 'off':
        await bot.send_message(query.from_user.id, 'Не включено',
                               )


@dp.callback_query_handler(filters.Regexp(r'default_list_(on|off)'))
async def default_list_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'default_list_(on|off)', query.data).groups()
    source = groups[0]
    if source == 'on':
        await bot.send_message(query.from_user.id, 'Загружено',
                               )
    elif source == 'off':
        await bot.send_message(query.from_user.id, 'Удален',
                               )
