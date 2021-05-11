import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.keyboards.inline.select_recipe import SelectRecipe
from app.misc import dp, bot
from app.recipe_parser.recipe_models import Recipe
from app.states.state_ingredients import IngredientsForRecipe


def recipe_helper(recipe: Recipe):
    if recipe.details is None:
        return f'{recipe.name}\n\n КБЖУ: {recipe.calories}\nВремя приготовления: {recipe.cooking_time}'
    return f'{recipe.name}\n\n КБЖУ: {recipe.calories}\nВремя приготовления: {recipe.cooking_time}\n\n{recipe.details}'


@dp.callback_query_handler(filters.Regexp(r'show_recipe_([0-9a-f]{32}\Z)'), state=IngredientsForRecipe.recipes)
async def recipe_callback_handler(query: types.CallbackQuery, state: FSMContext):
    recipe_id = re.match(r'show_recipe_([0-9a-f]{32}\Z)', query.data).groups()
    async with state.proxy() as list_recipes:
        recipes = list_recipes['recipes']
        recipe = next((x for x in recipes if x.id == recipe_id[0]), None)
        await bot.send_photo(query.from_user.id, recipe.image, recipe_helper(recipe), reply_markup=SelectRecipe.create(recipe))
    await query.answer()