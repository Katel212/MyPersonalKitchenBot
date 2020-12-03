import re
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.states import FridgeProductState


@dp.message_handler(lambda msg: re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', msg.text), state=FridgeProductState.expiration_date)
async def handler_fridge_expiration_date_state(msg: Message, state: FSMContext):
    try:
        datetime.strptime(msg.text, '%d.%m.%Y')
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату срока годности в формате "дд.мм.гггг"')
        return
    async with state.proxy() as data:
        data['expiration_date'] = msg.text
    await FridgeProductState.next()
    await msg.answer('Введите дату покупки продукта ("дд.мм.гггг", пропустить - /skip)')
