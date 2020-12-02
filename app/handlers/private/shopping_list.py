from datetime import datetime

from aiogram import types

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.misc import dp, db
from app.models import Product, User, ShoppingList, ShoppingListToProduct


def create_product(id: int, name: str, expiration_date: datetime, bought_date: datetime, info: str, user_id: int):
    product = Product()
    product.id = id
    product.name = name
    product.expiration_date = expiration_date
    product.bought_date = bought_date
    product.info = info
    product.user_id = user_id
    return product


@dp.message_handler(lambda message: message.text == 'Список покупок')
async def shopping_list_handler(msg: types.Message):
    products_with_trash = await User \
        .join(ShoppingList) \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .join(Product, Product.id == ShoppingListToProduct.product_id) \
        .select(User.id == msg.from_user.id) \
        .gino.all()

    products = [create_product(*list(item)[12:]) for item in products_with_trash]
    await msg.answer('Ваш список покупок:', reply_markup=ProductListKeyboard.create(products, 0, "shopping_list"))
