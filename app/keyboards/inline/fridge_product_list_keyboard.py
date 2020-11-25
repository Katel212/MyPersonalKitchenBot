import typing

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class FridgeProductListKeyboard(InlineKeyboardMarkup):

    @staticmethod
    def create(products: 'typing.List[Product]', page: int) -> InlineKeyboardMarkup:
        product_buttons = [InlineKeyboardButton(product.name, callback_data=f"show_fridge_{product.id}") for product in
                           products[page * 10:(page + 1) * 10]]

        previous_page_button = InlineKeyboardButton('<<', callback_data='previous_page_fridge')
        next_page_button = InlineKeyboardButton('>>', callback_data='next_page_fridge')
        add_button = InlineKeyboardButton('Добавить', callback_data='add_to_fridge')
        last_row_buttons = []
        if page != 0:
            last_row_buttons.append(previous_page_button)
        last_row_buttons.append(add_button)
        if (page + 1) * 10 < len(products):
            last_row_buttons.append(next_page_button)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[product_buttons, last_row_buttons])
        return keyboard
