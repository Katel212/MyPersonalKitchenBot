from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class MainKeyboard(ReplyKeyboardMarkup):

    @staticmethod
    def create() -> ReplyKeyboardMarkup:
        my_fridge_button = KeyboardButton("Мой холодильник")
        shopping_list_button = KeyboardButton("Список покупок")
        find_recipe_button = KeyboardButton("Подобрать рецепт")
        help_button = KeyboardButton("Помощь")
        settings_button = KeyboardButton("Настройки")
        row1 = [my_fridge_button, shopping_list_button]
        row2 = [find_recipe_button, help_button]
        row3 = [settings_button]
        keyboard = ReplyKeyboardMarkup([row1, row2,row3])
        return keyboard
