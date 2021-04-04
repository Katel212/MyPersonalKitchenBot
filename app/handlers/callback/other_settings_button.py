import re
from datetime import datetime, timedelta

from aiogram import types


from aiogram.dispatcher import filters

from app.misc import dp, bot

from app.keyboards.inline.automatic_setting_of_the_purchase_date_keyboard import \
    AutomaticSettingOfThePurchaseDateListKeyboard
from app.keyboards.inline.default_list_of_products_keyboard import DefaultListOfProductsListKeyboard
from app.models import Product


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
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Хлеб',
                                           expiration_date=datetime.today() + timedelta(days=1),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Мука пшеничная',
                                           expiration_date=datetime.today() + timedelta(days=183),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Сода',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Соль',
                                           expiration_date=datetime.today() + timedelta(days=730),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Сахар',
                                           expiration_date=datetime.today() + timedelta(days=730),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Черный перец',
                                           expiration_date=datetime.today() + timedelta(days=155),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Макароны',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Гречневая каша',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Рис',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Масло подсолнечное',
                                           expiration_date=datetime.today() + timedelta(days=45),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Масло сливочное',
                                           expiration_date=datetime.today() + timedelta(days=35),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Лук репчатый',
                                           expiration_date=datetime.today() + timedelta(days=12),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Чеснок',
                                           expiration_date=datetime.today() + timedelta(days=121),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Дрожжи',
                                           expiration_date=datetime.today() + timedelta(days=31),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Молоко',
                                           expiration_date=datetime.today() + timedelta(days=2),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Яйца(куриные)',
                                           expiration_date=datetime.today() + timedelta(days=7),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Чай',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Кофе',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        new_product = await Product.create(user_id=query.from_user.id,
                                           name='Яйца(куриные)',
                                           expiration_date=datetime.today() + timedelta(days=365),
                                           bought_date=datetime.today(),
                                           info='')
        await bot.send_message(query.from_user.id, 'Загружено',
                               )

    elif source == 'off':
        await bot.send_message(query.from_user.id, 'Удален',
                               )
