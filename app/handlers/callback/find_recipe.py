from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.keyboards.inline.recipes_keyboard import RecipesListKeyboard
from app.misc import dp, bot
from app.recipe_parser.parser import ParserHelper, Parser
from app.states.state_ingredients import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'find_recipe'), state=IngredientsForRecipe.ingredients)
async def find_recipe(query: types.CallbackQuery, state: FSMContext):
    await IngredientsForRecipe.next()
    async with state.proxy() as ingredients:
        await query.answer("Ищем рецепты...")
        ingredients_list = ingredients['ingredients']
        helper = ParserHelper(ingredients_list)
        search_url = await helper.get_search_string()
        parser = Parser(search_url)
        ingredients['recipes'] = parser.get_recipes()
        await bot.send_message(query.from_user.id, f'Возможные рецепты из {", ".join(ingredients_list)}:',
                               reply_markup=RecipesListKeyboard.create(ingredients['recipes'], 0))

