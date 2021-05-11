from datetime import *
import re

import dateutil
from aiogram.dispatcher import FSMContext
from aiogram.types import Message


from app.misc import dp
from app.models import Product
from app.states.state_change_product import ChangeProductState


@dp.message_handler(state=ChangeProductState.bought_date)
async def handler_change_bought_date_state(msg: Message, state: FSMContext):
    try:
        dateutil.parser.parse(msg.text)
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату срока годности')
        return
    async with state.proxy() as data:
        data['bought_date'] = msg.text
    bought_dat = dateutil.parser.parse(data['bought_date'])
    product = await Product.query.where(Product.id == int(ChangeProductState.id)).gino.first()
    await product.update(bought_date=bought_dat).apply()
    await state.finish()
    await msg.answer('Дата покупки успешно изменена!')
