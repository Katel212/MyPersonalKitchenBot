from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class WeeklyNotificationSettings(InlineKeyboardMarkup):
    @staticmethod
    def create():
        turn_on_button = InlineKeyboardButton('Включить',
                                              callback_data=f'week_on')
        turn_off_button = InlineKeyboardButton('Выключить', callback_data=f'week_off_')
        day_of_week_button = InlineKeyboardButton('Выбор дня недели',
                                                  callback_data=f'week_day')

        return InlineKeyboardMarkup(inline_keyboard=[[turn_on_button], [turn_off_button],
                                                     [day_of_week_button]
                                                     ])
