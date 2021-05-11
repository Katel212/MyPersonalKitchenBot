from datetime import datetime

import dateutil
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from dateutil import *
from app.misc import dp
from app.models import Product, UserSettings
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.info, commands='skip')
async def handler_fridge_skip_info_state(msg: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        data['info'] = None
        exp_date = None
        if data['expiration_date'] is not None:
            exp_date = dateutil.parser.parse(data['expiration_date'])
        user = await UserSettings.query.where(UserSettings.user_id == msg.from_user.id).gino.first()
        bought_date = None
        if not user.automatic_bought_date:
            if data['bought_date'] is not None:
                bought_date = dateutil.parser.parse(data['bought_date'])
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], expiration_date=exp_date,
                                           bought_date=bought_date, info=data['info'])
        await msg.answer("Продукт успешно добавлен в ваш холодильник!")
    await state.finish()
