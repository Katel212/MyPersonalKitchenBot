from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CaloriesKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        button1 = InlineKeyboardButton('100', callback_data='100_kcal')
        button2 = InlineKeyboardButton('200', callback_data='200_kcal')
        button3 = InlineKeyboardButton('300', callback_data='300_kcal')
        button4 = InlineKeyboardButton('400', callback_data='400_kcal')
        button5 = InlineKeyboardButton('500', callback_data='500_kcal')
        button6 = InlineKeyboardButton('600', callback_data='600_kcal')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3], [button4, button5, button6]])
        return keyboard
