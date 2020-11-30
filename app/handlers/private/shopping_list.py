import sqlalchemy
from aiogram import types

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.misc import dp
from app.models import Product, User, ShoppingList, ShoppingListToProduct


@dp.message_handler(lambda message: message.text == 'Список покупок')
async def shopping_list_handler(msg: types.Message):
    products = await ShoppingList.query \
        .join(ShoppingList, ShoppingList.user_id == User.id) \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .join(Product, Product.id == ShoppingListToProduct.product_id) \
        .select(User.id == msg.from_user.id) \
        .gino.all()
    await msg.answer('Ваш список покупок:', reply_markup=ProductListKeyboard.create(products, 0, "shopping_list"))
