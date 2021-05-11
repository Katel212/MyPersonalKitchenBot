from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.keyboards.inline.calories_keyboard import CaloriesKeyboard
from app.misc import dp, bot
from app.states import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'calories_keyboard'),state=IngredientsForRecipe.ingredients)
async def calories_keyboard_handler(query: types.CallbackQuery,state: FSMContext):
    await IngredientsForRecipe.next()
    await bot.send_message(query.from_user.id,'Выберите максимальноее число ккал в 100 гр блюда',reply_markup=CaloriesKeyboard.create())
    await query.answer()