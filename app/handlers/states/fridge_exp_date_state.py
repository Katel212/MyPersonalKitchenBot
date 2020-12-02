from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.expiration_date)
async def handler_fridge_expiration_date_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['expiration_date'] = msg.text
    await FridgeProductState.next()
    await msg.answer("Введите дату покупки продукта (пропустить - /skip)")
