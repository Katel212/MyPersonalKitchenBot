from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class ShoppingListProductInfoKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create(product: Product):
        delete_from_list_button = InlineKeyboardButton('Удалить из списка', callback_data=f'delete_from_shopping_list_{product.id}')
        buy_button = InlineKeyboardButton('Купить', callback_data=f'buy_{product.id}')
        return InlineKeyboardMarkup(inline_keyboard=[delete_from_list_button, buy_button])
