import datetime
import re

from aiogram import types
from aiogram.dispatcher import filters

from app.misc import dp, bot
from app.models import Product, ShoppingListToProduct


@dp.callback_query_handler(filters.Regexp(r'buy_(\d*)'))
async def buy_product(query: types.CallbackQuery):
    groups = re.match(r'buy_(\d*)', query.data).groups()
    product = await Product.query.where(Product.id == int(groups[0])).gino.first()
    await ShoppingListToProduct.delete.where(product.id == ShoppingListToProduct.product_id).gino.status()
    await product.update(bought_date=datetime.datetime.now()).apply()
    await bot.delete_message(query.from_user.id, query.message.message_id)
    await bot.send_message(query.from_user.id, f"Продукт \"{product.name}\" добавлен в ваш холодильник")
    await query.answer()
