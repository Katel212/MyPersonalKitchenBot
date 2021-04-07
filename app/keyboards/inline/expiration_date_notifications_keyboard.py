from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class ExpirationDateNotificationsListKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        turn_on_button = InlineKeyboardButton('Включить',
                                              callback_data=f'date_on')
        turn_off_button = InlineKeyboardButton('Выключить', callback_data=f'date_off')
        number_of_days_before_expiration_date_button = InlineKeyboardButton(
            'Количество дней до истечения срока годности',
            callback_data=f'date_settings')

        return InlineKeyboardMarkup(inline_keyboard=[[turn_on_button, turn_off_button],
                                                     [number_of_days_before_expiration_date_button]
                                                     ])
