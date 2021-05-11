import dateutil
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from app.misc import dp
from app.models import Product
from app.states import FridgeProductState


@dp.message_handler(Text(equals='/skipall', ignore_case=True), state=FridgeProductState.expiration_date)
async def fridge_skip_all_exp_handler(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], expiration_date=None,
                                           bought_date=None, info=None)
        await msg.answer("Продукт успешно добавлен в ваш холодильник!")
    await state.finish()


@dp.message_handler(Text(equals='/skipall', ignore_case=True), state=FridgeProductState.bought_date)
async def fridge_skip_all_bought_handler(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        exp_date = None
        if data['expiration_date'] is not None:
            exp_date = dateutil.parser.parse(data['expiration_date'])
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], expiration_date=exp_date,
                                           bought_date=None, info=None)
        await msg.answer("Продукт успешно добавлен в ваш холодильник!")

    await state.finish()