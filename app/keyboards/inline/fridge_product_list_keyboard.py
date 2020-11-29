import typing

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class ProductListKeyboard(InlineKeyboardMarkup):

    @staticmethod
    def create(products: 'typing.List[Product]', page: int, previous_button: str) -> InlineKeyboardMarkup:
        product_buttons = [[InlineKeyboardButton(product.name, callback_data=f"show_{previous_button}_{product.id}")] for product in
                           products[page * 10:(page + 1) * 10]]
        previous_page_button = InlineKeyboardButton('<<', callback_data=f'previous_page_{previous_button}')
        next_page_button = InlineKeyboardButton('>>', callback_data=f'next_page_{previous_button}')
        add_button = InlineKeyboardButton('Добавить', callback_data=f'add_to_{previous_button}')
        last_row_buttons = []
        if page != 0:
            last_row_buttons.append(previous_page_button)
        last_row_buttons.append(add_button)
        if (page + 1) * 10 < len(products):
            last_row_buttons.append(next_page_button)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[*product_buttons, last_row_buttons])
        return keyboard
