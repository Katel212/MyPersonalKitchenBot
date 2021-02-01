import re

from aiogram import types

from app.misc import dp
from app.states.state_change_product import ChangeProductState


@dp.message_handler(lambda msg: not re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', msg.text), state=ChangeProductState.bought_date)
async def handler_change_bought_date_error_state(msg: types.Message):
    return await msg.answer('Неправильный формат даты!\nВведите срок годности в формате "дд.мм.гггг"')
