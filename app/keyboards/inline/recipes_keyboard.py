from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.recipe_parser.recipe_models import Recipe


class RecipesListKeyboard(InlineKeyboardMarkup):

    @staticmethod
    def create(recipes: List[Recipe], page: int):
        recipe_buttons = [[InlineKeyboardButton(recipe.name, callback_data=f"show_recipe_{recipe.id}")] for recipe in
                          recipes[page * 10:(page + 1) * 10]]
        previous_page_button = InlineKeyboardButton('<<', callback_data=f'previous_page_recipes_{page}')
        next_page_button = InlineKeyboardButton('>>', callback_data=f'next_page_recipes_{page}')
        last_row_buttons = []
        if page != 0:
            last_row_buttons.append(previous_page_button)
        if (page + 1) * 10 < len(recipes):
            last_row_buttons.append(next_page_button)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[*recipe_buttons, last_row_buttons])
        return keyboard
