import re
from datetime import datetime

import dateutil
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.states import FridgeProductState
from dateutil import *


@dp.message_handler(state=FridgeProductState.bought_date)
async def handler_fridge_bought_date_state(msg: Message, state: FSMContext):
    try:
        dateutil.parser.parse(msg.text)
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату покупки')
        return
    async with state.proxy() as data:
        data['bought_date'] = msg.text
    await FridgeProductState.next()
    await msg.answer("Введите дополнительную информацию о продукте (пропустить - /skip)")
