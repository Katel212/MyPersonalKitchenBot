from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class AutomaticSettingOfThePurchaseDateListKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        turn_on_button = InlineKeyboardButton('Включить',
                                              callback_data=f'purchase_date_list_on')
        turn_off_button = InlineKeyboardButton('Выключить', callback_data=f'purchase_date_list_off')
        back_button = InlineKeyboardButton('<<', callback_data='back_to_other_settings')

        return InlineKeyboardMarkup(inline_keyboard=[[turn_on_button, turn_off_button],[back_button]])
