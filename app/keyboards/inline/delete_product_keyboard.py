from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class ConfirmDeleteProductKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create(product: Product, info_message: int):
        delete_yes_button = InlineKeyboardButton('Да', callback_data=f'delete_yes_{product.id}_{info_message}')
        delete_no_button = InlineKeyboardButton('Нет', callback_data=f'delete_no_{product.id}')
        return InlineKeyboardMarkup(inline_keyboard=[[delete_yes_button, delete_no_button]])
