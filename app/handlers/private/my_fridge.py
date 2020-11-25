from aiogram import types

from app.keyboards.inline.fridge_product_list_keyboard import FridgeProductListKeyboard
from app.misc import dp


@dp.message_handler(lambda message: message.text == 'Мой холодильник' and message.text)
async def my_fridge_handler(msg: types.Message):
    # TODO: crate default products list
    await msg.answer('Список ваших продуктов:', reply_markup=FridgeProductListKeyboard.create())
