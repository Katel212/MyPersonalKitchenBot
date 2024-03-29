from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class DefaultListOfProductsListKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        turn_on_button = InlineKeyboardButton('Загрузить',
                                              callback_data=f'default_list_on')
        turn_off_button = InlineKeyboardButton('Удалить', callback_data=f'default_list_off')
        back_button = InlineKeyboardButton('<<', callback_data='back_to_other_settings')
        return InlineKeyboardMarkup(inline_keyboard=[[turn_on_button, turn_off_button],[back_button]])
