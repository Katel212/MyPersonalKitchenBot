import re

from aiogram import types
from aiogram.dispatcher import filters

from app.keyboards.inline.add_product_method import AddProductMethod
from app.misc import dp, bot


@dp.callback_query_handler(filters.Regexp(r'add_to_(fridge|shopping_list)'))
async def add_to_callback_handler(query: types.CallbackQuery):
    info = re.findall(r'(fridge|shopping_list)', query.data)
    await bot.send_message(query.from_user.id,
                           "Выберите тип добавления продукта",
                           reply_markup=AddProductMethod.create(info, query.message.message_id))
    await query.answer()
