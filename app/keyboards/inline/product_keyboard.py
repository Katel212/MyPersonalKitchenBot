from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class ProductKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create(product: Product):
        delete_button = InlineKeyboardButton('Удалить', callback_data=f'delete_{product.id}')
        change_button = InlineKeyboardButton('Изменить', callback_data=f'change_{product.id}')
        add_to_shop_list_button = InlineKeyboardButton('Добавить в список покупок', callback_data=f'add_to_shop_list_{product.id}')
        return InlineKeyboardMarkup(inline_keyboard=[[delete_button, change_button], [add_to_shop_list_button]])
