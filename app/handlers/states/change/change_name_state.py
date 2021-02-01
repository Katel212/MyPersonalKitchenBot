from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product
from app.states.state_change_product import ChangeProductState


@dp.message_handler(state=ChangeProductState.name)
async def handler_change_name_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = msg.text
    product = await Product.query.where(Product.id == int(ChangeProductState.id)).gino.first()
    await product.update(name = data['name']).apply()
    await state.finish()
    await msg.answer('Название успешно изменено!')

