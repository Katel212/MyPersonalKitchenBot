from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from app.misc import dp


@dp.message_handler(state='*', commands='exit')
@dp.message_handler(Text(equals='exit', ignore_case=True), state='*')
async def exit_handler(message: types.Message, state: FSMContext):

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Добавление отменено.')
