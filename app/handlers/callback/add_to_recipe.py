import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.misc import dp
from app.states.state_ingredients import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'add_to_recipe_(\w*)'), state=IngredientsForRecipe.ingredients)
async def add_to_recipe(query: types.CallbackQuery, state: FSMContext):
    name = re.match(r'add_to_recipe_(\w*)', query.data).groups()
    await query.answer()
    async with state.proxy() as ingredients:
        if len(ingredients.get("ingredients", [])) == 0:
            ingredients["ingredients"] = []
        ingredients["ingredients"].append(name[0])
