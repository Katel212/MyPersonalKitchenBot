from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



class AddProductPhotoErrorFridge(InlineKeyboardMarkup):
    @staticmethod
    def create():
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'fridge\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'fridge\']')
        return InlineKeyboardMarkup(inline_keyboard=[[reset_button, add_typing_button]])

class AddProductPhotoGoodFridge(InlineKeyboardMarkup):
    @staticmethod
    def create(food: str):
        name_is_ok = InlineKeyboardButton('Да', callback_data=f'add_product_photo_name_ok_[\'fridge\']+{food}')
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'fridge\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'fridge\']')
        return InlineKeyboardMarkup(inline_keyboard=[[name_is_ok, reset_button],[add_typing_button]])

class AddProductPhotoErrorShoppingList(InlineKeyboardMarkup):
    @staticmethod
    def create():
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'shopping_list\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'shopping_list\']')
        return InlineKeyboardMarkup(inline_keyboard=[[reset_button, add_typing_button]])

class AddProductPhotoGoodShoppingList(InlineKeyboardMarkup):
    @staticmethod
    def create(food: str):
        name_is_ok = InlineKeyboardButton('Да', callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{food}')
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'shopping_list\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'shopping_list\']')
        return InlineKeyboardMarkup(inline_keyboard=[[name_is_ok, reset_button], [add_typing_button]])
