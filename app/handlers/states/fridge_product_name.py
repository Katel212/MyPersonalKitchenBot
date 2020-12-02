from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.name)
async def handle_fridge_product_name_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text

    await FridgeProductState.next()
    await msg.answer("Введите срок годности продукта (пропустить - /skip)")
