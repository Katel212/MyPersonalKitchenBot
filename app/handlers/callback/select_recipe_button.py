import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.misc import dp, bot
from app.recipe_parser.parser import Parser
from app.recipe_parser.recipe_models import RecipeDetails
from app.states import IngredientsForRecipe


def recipe_details_helper(rd: RecipeDetails):
    # steps = rd.instructions
    ingredients = ", ".join(map(lambda x: str(x), rd.ingredients))
    if rd.instructions is None:
        steps = '\n'.join(rd.steps)
        return f'{rd.name}\n\nКБЖУ: {rd.weight} гр - {rd.PFC}\nВремя приготовления {rd.cooking_time}\n\nДля {rd.portions_count} порций: {ingredients}\n\n{steps}'
    return f'{rd.name}\n\nКБЖУ: {rd.weight} гр - {rd.PFC}\nВремя приготовления {rd.cooking_time}\n\nДля {rd.portions_count} порций: {ingredients}\n\n{rd.instructions}'


@dp.callback_query_handler(filters.Regexp(r'select_recipe_([0-9a-f]{32}\Z)'), state=IngredientsForRecipe.recipes)
async def select_recipe(query: types.CallbackQuery, state: FSMContext):
    recipe_id = re.match(r'select_recipe_([0-9a-f]{32}\Z)', query.data).groups()
    async with state.proxy() as list_recipes:
        recipes = list_recipes['recipes']
        recipe = next((x for x in recipes if x.id == recipe_id[0]), None)
        recipe_details = await Parser.get_recipe_details(recipe)
        await bot.send_message(query.from_user.id, recipe_details_helper(recipe_details))
    await state.finish()
    await query.answer()
