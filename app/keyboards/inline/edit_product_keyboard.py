from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.models import Product


class ChangeInfoAboutProductKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create(product: Product):
        change_name_button = InlineKeyboardButton('Название', callback_data=f'change_name_{product.id}')
        change_expiration_date_button = InlineKeyboardButton('Срок годности', callback_data=f'change_expiration_date_{product.id}')
        change_info_button = InlineKeyboardButton('Информацию о продукте', callback_data=f'change_info_{product.id}')
        change_bought_time_button = InlineKeyboardButton('Дату покупки', callback_data=f'change_bought_time_{product.id}')
        return InlineKeyboardMarkup(
            inline_keyboard=[[change_name_button, change_expiration_date_button], [change_bought_time_button, change_info_button]])
