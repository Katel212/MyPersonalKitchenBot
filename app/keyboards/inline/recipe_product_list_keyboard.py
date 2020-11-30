import typing

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class RecipeProductListKeyboard(InlineKeyboardMarkup):

    @staticmethod
    def create(products: 'typing.List[Product]', page: int, source: str) -> InlineKeyboardMarkup:
        products_for_buttons = products[page * 10:(page + 1) * 10]

        product_buttons = [[InlineKeyboardButton(product.name, callback_data=f"add_to_recipe_{product.id}")] for product in products_for_buttons]
        choose_all_button = InlineKeyboardButton('Выбрать всё', callback_data=f'select_all_product_for_recipe')
        search_button = InlineKeyboardButton('Поиск', callback_data=f'find_recipe')
        previous_page_button = InlineKeyboardButton('<<', callback_data=f'previous_page_{source}_{page}')
        next_page_button = InlineKeyboardButton('>>', callback_data=f'next_page_{source}_{page}')
        second_last_row_buttons = []
        if page != 0:
            second_last_row_buttons.append(previous_page_button)
        if (page + 1) * 10 < len(products):
            second_last_row_buttons.append(next_page_button)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[*product_buttons, second_last_row_buttons, [choose_all_button, search_button]])
        return keyboard
