from typing import List

from aiogram.dispatcher.filters.state import StatesGroup, State


class IngredientsForRecipe(StatesGroup):
    ingredients = State()
    recipes = State()

