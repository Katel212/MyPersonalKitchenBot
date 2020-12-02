from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp, storage
from app.states import ShopListProductState


@dp.message_handler(state=ShopListProductState.name)
async def handle_shopping_list_product_name_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text

    await ShopListProductState.next()
    await msg.answer("Введите информацию о продукте (пропустить - /skip)")
