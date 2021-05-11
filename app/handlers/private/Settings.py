from aiogram import types
from aiogram.dispatcher import FSMContext

from app.keyboards.inline.settings_keyboard import SettingsListKeyboard
from app.misc import dp

@dp.message_handler(lambda message: message.text == 'Настройки')
async def settings_handler(msg: types.Message):
    await msg.answer('Возможные настройки:', reply_markup=SettingsListKeyboard.create())


@dp.message_handler(lambda message: message.text == 'Настройки',state='*')
async def settings_handler_st(msg: types.Message,state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await msg.answer('Возможные настройки:', reply_markup=SettingsListKeyboard.create())