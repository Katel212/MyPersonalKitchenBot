from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.info)
async def handler_fridge_product_info_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = msg.text
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], expiration_date=data['expiration_date'],
                                           bought_date=data['bought_date'], info=data['info'])
    await state.finish()
