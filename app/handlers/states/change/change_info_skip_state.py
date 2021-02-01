from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.states.state_change_product import ChangeProductState


@dp.message_handler(state=ChangeProductState.info, commands='skip')
async def handler_change_info_skip_state(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer('Ладно...')

