from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CaloriesKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        button1 = InlineKeyboardButton('100', callback_data='100_kcal')
        button2 = InlineKeyboardButton('150', callback_data='150_kcal')
        button3 = InlineKeyboardButton('200', callback_data='200_kcal')
        button4 = InlineKeyboardButton('250', callback_data='250_kcal')
        button5 = InlineKeyboardButton('300', callback_data='300_kcal')
        button6 = InlineKeyboardButton('350', callback_data='350_kcal')
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3], [button4, button5, button6]])
        return keyboard
