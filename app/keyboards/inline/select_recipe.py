from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.recipe_parser.recipe_models import Recipe


class SelectRecipe(InlineKeyboardMarkup):

    @staticmethod
    def create(recipe: Recipe):
        select_button = InlineKeyboardButton('Выбрать', callback_data=f'select_recipe_{recipe.id}')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[select_button]])
        return keyboard
