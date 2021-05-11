import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.misc import dp, bot
from app.states import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'(\d*)_kcal'), state=IngredientsForRecipe.kcal)
async def calories_filter_handler(query: types.CallbackQuery, state: FSMContext):
    groups = re.match(r'(\d*)_kcal', query.data).groups()
    async with state.proxy() as kcal:
        kcal['kcal'] = groups[0]
    await IngredientsForRecipe.previous()
    await query.answer()
    await bot.delete_message(query.from_user.id, query.message.message_id)