from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from app.keyboards.reply.main_keyboard import MainKeyboard
from app.misc import dp


@dp.message_handler(CommandStart())
async def command_start_handler(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}!\n\nЯ бот, который поможет тебе следить за содержимым твоего холодильника. Список всех доступных на данный момент функций можно посмотреть по кнопке "Помощь".', reply_markup=MainKeyboard.create())
