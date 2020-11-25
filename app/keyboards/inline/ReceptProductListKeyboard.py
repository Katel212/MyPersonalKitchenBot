import typing

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class ProductListKeyboard(InlineKeyboardMarkup):

    @staticmethod
    def create(products: 'typing.List[Product]', page: int) -> InlineKeyboardMarkup:
        product_buttons = [InlineKeyboardButton(product.name, callback_data=f"show_{product.id}") for product in
                           products[page * 10:(page + 1) * 10]]
        choose_all_button = InlineKeyboardButton('Выбрать всё', callback_data=f'previous_page_')
        search_button = InlineKeyboardButton('Поиск', callback_data=f'next_page_fridge')
        previous_page_button = InlineKeyboardButton('<<', callback_data=f'previous_page_')
        next_page_button = InlineKeyboardButton('>>', callback_data=f'next_page_fridge')
        add_button = InlineKeyboardButton('Добавить', callback_data=f'add_to_fridge')
        second_last_row_buttons = []
        if page != 0:
            second_last_row_buttons.append(previous_page_button)
        second_last_row_buttons.append(add_button)
        if (page + 1) * 10 < len(products):
            second_last_row_buttons.append(next_page_button)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[product_buttons, second_last_row_buttons, [choose_all_button, search_button]])
        return keyboard


