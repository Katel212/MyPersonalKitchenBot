from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product, UserSettings
from app.states import FridgeProductState


@dp.message_handler(state=FridgeProductState.expiration_date, commands='skip')
async def handler_fridge_skip_exp_date_state(msg: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        data['expiration_date'] = None
    await FridgeProductState.next()
    user = await UserSettings.query.where(UserSettings.user_id == msg.from_user.id).gino.first()
    if user.automatic_bought_date:
        async with state.proxy() as data:
            data['bought_date'] = str(datetime.now().date())
        await FridgeProductState.next()
        await msg.answer("Введите дополнительную информацию о продукте (пропустить - /skip)")
    else:
        await msg.answer('Введите дату покупки продукта (пропустить - /skip, пропустить остальные шаги /skipall)')

