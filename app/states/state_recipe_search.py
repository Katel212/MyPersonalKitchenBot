from aiogram.dispatcher.filters.state import StatesGroup, State


class RecipeSearch(StatesGroup):
    recipes = State()
