import re
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.states import FridgeProductState


@dp.message_handler(lambda msg: re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', msg.text), state=FridgeProductState.bought_date)
async def handler_fridge_bought_date_state(msg: Message, state: FSMContext):
    try:
        datetime.strptime(msg.text, '%d.%m.%Y')
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату покупки в формате "дд.мм.гггг"')
        return
    async with state.proxy() as data:
        data['bought_date'] = msg.text
    await FridgeProductState.next()
    await msg.answer("Введите дополнительную информацию о продукте (пропустить - /skip)")
