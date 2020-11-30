from aiogram import types

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.misc import dp, db
from app.models import Product


@dp.message_handler(lambda message: message.text == 'Мой холодильник')
async def my_fridge_handler(msg: types.Message):
    products = await Product.query.where(Product.user_id == msg.from_user.id).gino.all()
    await msg.answer('Список ваших продуктов:', reply_markup=ProductListKeyboard.create(products, 0, "fridge"))