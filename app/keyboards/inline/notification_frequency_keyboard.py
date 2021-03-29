from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class NotificationFrequencySettingsKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        turn_on_button = InlineKeyboardButton('Включить',
                                              callback_data=f'freq_on')
        turn_off_button = InlineKeyboardButton('Выключить', callback_data=f'freq_off')
        number_of_notifications_per_day_button = InlineKeyboardButton('Количество дней между уведомлениями',
                                                                      callback_data=f'freq_number_of_notifications')

        return InlineKeyboardMarkup(inline_keyboard=[[turn_on_button], [turn_off_button],
                                                     [number_of_notifications_per_day_button]
                                                     ])
