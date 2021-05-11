import re
from datetime import datetime

import dateutil
from dateutil.parser import *
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.models import UserSettings
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.expiration_date)
async def handler_fridge_expiration_date_state(msg: Message, state: FSMContext):
    try:
        dateutil.parser.parse(msg.text)
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату срока годности')
        return
    if dateutil.parser.parse(msg.text) < datetime.now():
        await msg.answer('Срок годности уже истек!\n\nНажмите /cancel, чтоб отменить добавление, или введите информацию о продукте для продолжения')
        async with state.proxy() as data:
            data['expiration_date'] = msg.text
        await FridgeProductState.next()
        return
    async with state.proxy() as data:
        data['expiration_date'] = msg.text
    await FridgeProductState.next()
    user = await UserSettings.query.where(UserSettings.user_id == msg.from_user.id).gino.first()
    if user.automatic_bought_date:
        async with state.proxy() as data:
            data['bought_date'] = str(datetime.now().date())
        await FridgeProductState.next()
        await msg.answer("Введите дополнительную информацию о продукте (пропустить - /skip)")
    else:
        await msg.answer('Введите дату покупки продукта (пропустить - /skip, пропустить остальные шаги /skipall)')
