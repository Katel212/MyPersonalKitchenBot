from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.states.state_change_product import ChangeProductState


@dp.message_handler(state=ChangeProductState.expiration_date, commands='cancel')
async def handler_change_cancel_exp_date_state(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer('Изменение отменено')

