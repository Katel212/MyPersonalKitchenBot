import re
from datetime import datetime


from aiogram import types
from aiogram.dispatcher import filters

from app.keyboards.inline.product_for_shop_list_keyboard import ShoppingListProductInfoKeyboard
from app.keyboards.inline.product_keyboard import ProductKeyboard
from app.misc import dp, bot
from app.models import Product
from dateutil.parser import parse


def create_info_product_message(name: str, exp_date: datetime, bought_date: datetime, info: str):
    bubble = f'{name}\n'
    if exp_date is not None:
        e = parse(str(exp_date)).strftime('%d.%m.%Y')
        bubble += f'Срок годности: до {e}\n'
    if bought_date is not None:
        b = parse(str(bought_date)).strftime('%d.%m.%Y')
        bubble += f'Дата покупки: {b}\n'
    bubble += info if info else ''
    return bubble


@dp.callback_query_handler(filters.Regexp(r'show_(fridge|shopping_list)_(\d*)'))
async def handler_product_button(query: types.CallbackQuery):
    groups = re.match(r'show_(fridge|shopping_list)_(\d*)', query.data).groups()
    product = await Product.query.where(Product.id == int(groups[1])).gino.first()
    if groups[0] == 'fridge':
        await bot.send_message(query.from_user.id,
                               create_info_product_message(product.name, product.expiration_date, product.bought_date, product.info),
                               reply_markup=ProductKeyboard.create(product))
    elif groups[0] == 'shopping_list':
        await bot.send_message(query.from_user.id,
                               create_info_product_message(product.name, product.expiration_date, product.bought_date, product.info),
                               reply_markup=ShoppingListProductInfoKeyboard.create(product))
    await query.answer()