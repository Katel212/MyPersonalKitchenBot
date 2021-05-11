from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class AddProductMethodChoice(InlineKeyboardMarkup):
    @staticmethod
    def create(Info: str, info_message: int):
        add_check_button = InlineKeyboardButton('Чек', callback_data=f'add_product_photo_check_{Info}')
        add_photo_button = InlineKeyboardButton('Продукт', callback_data=f'add_product_photo_{Info}')
        return InlineKeyboardMarkup(inline_keyboard=[[add_check_button, add_photo_button]])
