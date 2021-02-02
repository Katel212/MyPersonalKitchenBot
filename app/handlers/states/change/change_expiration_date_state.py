from datetime import *
import re

from aiogram.dispatcher import FSMContext
from aiogram.types import Message


from app.misc import dp
from app.models import Product
from app.states.state_change_product import ChangeProductState


@dp.message_handler(lambda msg: re.search(r'^\d{1,2}\.\d{1,2}\.\d{4}$', msg.text), state=ChangeProductState.expiration_date)
async def handler_change_expiration_date_state(msg: Message, state: FSMContext):
    try:
        datetime.strptime(msg.text, '%d.%m.%Y')
    except ValueError:
        await msg.answer('Такой даты не существует!\nВведите корректную дату срока годности в формате "дд.мм.гггг"')
        return
    async with state.proxy() as data:
        data['expiration_date'] = msg.text
    date_format = '%d.%m.%Y' 
    exp_date = datetime.strptime(data['expiration_date'], date_format)
    product = await Product.query.where(Product.id == int(ChangeProductState.id)).gino.first()
    await product.update(expiration_date = exp_date).apply()
    await state.finish()
    await msg.answer('Срок годности успешно изменён!')