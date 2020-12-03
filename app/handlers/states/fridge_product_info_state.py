from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.info)
async def handler_fridge_product_info_state(msg: Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = msg.text
        date_format = '%d.%m.%Y'
        exp_date = None
        if data['expiration_date'] is not None:
            exp_date = datetime.strptime(data['expiration_date'], date_format)
        bought_date = None
        if data['bought_date'] is not None:
            bought_date = datetime.strptime(data['bought_date'], date_format)
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], expiration_date=exp_date,
                                           bought_date=bought_date, info=data['info'])
        await msg.answer("Продукт успешно добавлен в ваш холодильник!")

    await state.finish()
