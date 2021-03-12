from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class SettingsListKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        notification_settings_button = InlineKeyboardButton('Настройка уведомлений',
                                                            callback_data=f'settings_notification_settings')
        other_button = InlineKeyboardButton('Другое', callback_data=f'settings_other')
        return InlineKeyboardMarkup(inline_keyboard=[[notification_settings_button], [other_button]])
