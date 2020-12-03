import re

from aiogram import types

from app.misc import dp
from app.states import FridgeProductState


@dp.message_handler(lambda msg: not re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', msg.text), state=FridgeProductState.expiration_date)
async def handler_fridge_expiration_date_error(msg: types.Message):
    return await msg.answer('Неправильный формат даты!\nВведите срок годности в формате "дд.мм.гггг"')
