from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class AddProductMethod(InlineKeyboardMarkup):
    @staticmethod
    def create(Info: str, info_message: int):
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_{Info}')
        add_photo_button = InlineKeyboardButton('Сфотографировать', callback_data=f'add_product_photo_{Info}')
        return InlineKeyboardMarkup(inline_keyboard=[[add_typing_button, add_photo_button]])
