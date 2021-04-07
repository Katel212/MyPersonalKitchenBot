import re

from aiogram import types
from aiogram.dispatcher import filters

from app.misc import dp, bot
from app.models import Product, ShoppingList, ShoppingListToProduct


@dp.callback_query_handler(filters.Regexp(r'add_to_shop_list_(\d*)'))
async def add_to_shop_list_from_fridge(query: types.CallbackQuery):
    groups = re.match(r'add_to_shop_list_(\d*)', query.data).groups()
    product = await Product.query.where(Product.id == int(groups[0])).gino.first()
    shop_list = await ShoppingList.query.where(ShoppingList.user_id == query.from_user.id).gino.first()
    new_product = await Product.create(user_id=query.from_user.id, name=product.name, info=None)
    await ShoppingListToProduct.create( product_id=new_product.id, shopping_list_id=shop_list.id)
    await bot.send_message(query.from_user.id,"Продукт добавлен в список покупок")

