from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.info, commands='skip')
async def handler_fridge_skip_info_state(msg: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        data['info'] = None
        date_format = '%d.%m.%Y'
        exp_date = datetime.strptime(data['expiration_date'], date_format)
        bought_date = datetime.strptime(data['bought_date'], date_format)
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], expiration_date=exp_date,
                                           bought_date=bought_date, info=data['info'])
        await msg.answer("Продукт успешно добавлен в ваш холодильник!")
    await state.finish()
