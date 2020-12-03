from aiogram import types

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.misc import dp
from app.models import Product, ShoppingList, ShoppingListToProduct


@dp.message_handler(lambda message: message.text == 'Мой холодильник')
async def my_fridge_handler(msg: types.Message):
    products = await Product.query.where(Product.user_id == msg.from_user.id).gino.all()
    shopping_list_product_connections = await ShoppingList \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .select(ShoppingList.user_id == msg.from_user.id) \
        .gino.all()
    shopping_list_product_ids = [data[3] for data in shopping_list_product_connections]
    products = list(filter(lambda item: item.id not in shopping_list_product_ids, products))
    await msg.answer('Список ваших продуктов:', reply_markup=ProductListKeyboard.create(products, 0, "fridge"))
