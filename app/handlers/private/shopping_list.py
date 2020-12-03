from datetime import datetime

from aiogram import types

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.misc import dp, db
from app.models import Product, User, ShoppingList, ShoppingListToProduct




@dp.message_handler(lambda message: message.text == 'Список покупок')
async def shopping_list_handler(msg: types.Message):
    products_with_trash = await User \
        .join(ShoppingList) \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .join(Product, Product.id == ShoppingListToProduct.product_id) \
        .select(User.id == msg.from_user.id) \
        .gino.all()

    products = [Product.create_product(*list(item)[12:]) for item in products_with_trash]
    await msg.answer('Ваш список покупок:', reply_markup=ProductListKeyboard.create(products, 0, "shopping_list"))
