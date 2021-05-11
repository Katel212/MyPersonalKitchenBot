from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class NotificationSettingsListKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        notification_frequency_button = InlineKeyboardButton('Частота уведомлений',
                                                             callback_data=f'notification_frequency')
        time_to_expiration_date_button = InlineKeyboardButton('Время до конца срока годности',
                                                              callback_data=f'time_to_expiration_date')
        weekly_notification_button = InlineKeyboardButton('Еженедельное уведомление',
                                                          callback_data=f'weekly_notification')
        disable_notifications_completely_button = InlineKeyboardButton('Полное отключение уведомлений',
                                                                       callback_data=f'disable_notifications_completely')
        back_button = InlineKeyboardButton('<<',callback_data='back_to_settings')
        return InlineKeyboardMarkup(inline_keyboard=[[notification_frequency_button], [time_to_expiration_date_button],
                                                     [weekly_notification_button],
                                                     [disable_notifications_completely_button],[back_button]])
