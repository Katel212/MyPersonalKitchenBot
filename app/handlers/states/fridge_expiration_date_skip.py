from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.expiration_date, commands='skip')
async def handler_fridge_skip_exp_date_state(msg: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        data['expiration_date'] = None
    await FridgeProductState.next()
    await msg.answer("Введите дату покупки продукта (пропустить - /skip)")

