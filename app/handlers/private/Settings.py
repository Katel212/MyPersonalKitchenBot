from aiogram import types
from app.keyboards.inline.settings_keyboard import SettingsListKeyboard
from app.misc import dp


@dp.message_handler(lambda message: message.text == 'Настройки')
async def settings_handler(msg: types.Message):
    await msg.answer('Возможные настройки:', reply_markup=SettingsListKeyboard.create())
