from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.bought_date)
async def handler_fridge_bought_date_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['bought_date'] = msg.text
    await FridgeProductState.next()
    await msg.answer("Введите дополнительную информацию о продукте (пропустить - /skip)")
