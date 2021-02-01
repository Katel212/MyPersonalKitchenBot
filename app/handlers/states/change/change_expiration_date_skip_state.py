from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.states.state_change_product import ChangeProductState


@dp.message_handler(state=ChangeProductState.expiration_date, commands='skip')
async def handler_change_skip_exp_date_state(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer('Ладно...')

