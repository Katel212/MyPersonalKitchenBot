import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.keyboards.inline.recipes_keyboard import RecipesListKeyboard
from app.misc import dp, bot
from app.states import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'(previous|next)_page_recipes_(\d+)'), state=IngredientsForRecipe.recipes)
async def change_page_recipe(query: types.CallbackQuery, state: FSMContext):
    groups = re.match(r'(previous|next)_page_recipes_(\d+)', query.data).groups()
    new_page = 0
    if groups[0] == 'previous':
        new_page = int(groups[1]) - 1
    elif groups[0] == 'next':
        new_page = int(groups[1])+1
    async with state.proxy() as recipes:
        # RecipesListKeyboard.create(recipes['recipes'], new_page)
        await bot.edit_message_reply_markup(query.from_user.id,query.message.message_id,reply_markup=RecipesListKeyboard.create(recipes['recipes'], new_page))
