import re
from datetime import datetime

import dateutil
from dateutil.parser import *
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.expiration_date)
async def handler_fridge_expiration_date_state(msg: Message, state: FSMContext):
    try:
        dateutil.parser.parse(msg.text)
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату срока годности в формате "дд.мм.гггг"')
        return
    async with state.proxy() as data:
        data['expiration_date'] = msg.text
    await FridgeProductState.next()
    await msg.answer('Введите дату покупки продукта (пропустить - /skip)')
