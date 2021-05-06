from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard


class AddProductPhotoErrorFridge(InlineKeyboardMarkup):
    @staticmethod
    def create():
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'fridge\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'fridge\']')
        return InlineKeyboardMarkup(inline_keyboard=[[reset_button, add_typing_button]])


class AddProductPhotoGoodFridge(InlineKeyboardMarkup):
    @staticmethod
    def create(foods: list):
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'fridge\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную',
                                                 callback_data=f'add_product_typing_[\'fridge\']')
        inline_kb_full = InlineKeyboardMarkup(row_width=1)
        if len(foods) == 1:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            inline_kb_full.add(product_one)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 2:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            inline_kb_full.add(product_one, product_two)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) >= 3:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            inline_kb_full.add(product_one, product_two, product_three)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full


class AddProductPhotoErrorShoppingList(InlineKeyboardMarkup):
    @staticmethod
    def create():
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'shopping_list\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'shopping_list\']')
        return InlineKeyboardMarkup(inline_keyboard=[[reset_button, add_typing_button]])


class AddProductPhotoGoodShoppingList(InlineKeyboardMarkup):
    @staticmethod
    def create(foods: list):
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_[\'shopping_list\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную',
                                                 callback_data=f'add_product_typing_[\'shopping_list\']')
        inline_kb_full = InlineKeyboardMarkup(row_width=1)
        if len(foods) == 1:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            inline_kb_full.add(product_one)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 2:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            inline_kb_full.add(product_one, product_two)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) >= 3:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            inline_kb_full.add(product_one, product_two, product_three)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full


class AddProductPhotoCheckErrorFridge(InlineKeyboardMarkup):
    @staticmethod
    def create():
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_check_[\'fridge\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'fridge\']')
        return InlineKeyboardMarkup(inline_keyboard=[[reset_button, add_typing_button]])


class AddProductPhotoCheckErrorShoplist(InlineKeyboardMarkup):
    @staticmethod
    def create():
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_check_[\'shopping_list\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную', callback_data=f'add_product_typing_[\'shopping_list\']')
        return InlineKeyboardMarkup(inline_keyboard=[[reset_button, add_typing_button]])


class AddProductPhotoCheckGoodFridge(InlineKeyboardMarkup):
    @staticmethod
    def create(foods: list):
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_check_[\'fridge\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную',
                                                 callback_data=f'add_product_typing_[\'fridge\']')
        inline_kb_full = InlineKeyboardMarkup(row_width=1)
        if len(foods) == 1:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            inline_kb_full.add(product_one)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 2:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            inline_kb_full.add(product_one, product_two)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 3:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2], callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            inline_kb_full.add(product_one, product_two, product_three)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 4:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[3]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 5:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[4]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.add(product_five)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 6:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[4]}')
            product_six = InlineKeyboardButton(foods[5],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[5]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(product_five, product_six)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 7:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[4]}')
            product_six = InlineKeyboardButton(foods[5],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[5]}')
            product_seven = InlineKeyboardButton(foods[6],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[6]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(product_five, product_six)
            inline_kb_full.add(product_seven)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) >= 8:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[4]}')
            product_six = InlineKeyboardButton(foods[5],
                                               callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[5]}')
            product_seven = InlineKeyboardButton(foods[6],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[6]}')
            product_eight = InlineKeyboardButton(foods[7],
                                                 callback_data=f'add_product_photo_name_ok_[\'fridge\']+{foods[7]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(product_five, product_six)
            inline_kb_full.row(product_seven, product_eight)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full


class AddProductPhotoCheckGoodShoplist(InlineKeyboardMarkup):
    @staticmethod
    def create(foods: list):
        reset_button = InlineKeyboardButton('Повторить', callback_data=f'add_product_photo_check_[\'shopping_list\']')
        add_typing_button = InlineKeyboardButton('Ввести вручную',
                                                 callback_data=f'add_product_typing_[\'shopping_list\']')
        inline_kb_full = InlineKeyboardMarkup(row_width=1)
        if len(foods) == 1:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            inline_kb_full.add(product_one)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 2:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1], callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            inline_kb_full.add(product_one, product_two)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 3:
            product_one = InlineKeyboardButton(foods[0], callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1], callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2], callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            inline_kb_full.add(product_one, product_two, product_three)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 4:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[3]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 5:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[4]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.add(product_five)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 6:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[4]}')
            product_six = InlineKeyboardButton(foods[5],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[5]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(product_five, product_six)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) == 7:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[4]}')
            product_six = InlineKeyboardButton(foods[5],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[5]}')
            product_seven = InlineKeyboardButton(foods[6],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[6]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(product_five, product_six)
            inline_kb_full.add(product_seven)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full
        if len(foods) >= 8:
            product_one = InlineKeyboardButton(foods[0],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[0]}')
            product_two = InlineKeyboardButton(foods[1],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[1]}')
            product_three = InlineKeyboardButton(foods[2],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[2]}')
            product_four = InlineKeyboardButton(foods[3],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[3]}')
            product_five = InlineKeyboardButton(foods[4],
                                                callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[4]}')
            product_six = InlineKeyboardButton(foods[5],
                                               callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[5]}')
            product_seven = InlineKeyboardButton(foods[6],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[6]}')
            product_eight = InlineKeyboardButton(foods[7],
                                                 callback_data=f'add_product_photo_name_ok_[\'shopping_list\']+{foods[7]}')
            inline_kb_full = InlineKeyboardMarkup(row_width=2)
            inline_kb_full.row(product_one, product_two)
            inline_kb_full.row(product_three, product_four)
            inline_kb_full.row(product_five, product_six)
            inline_kb_full.row(product_seven, product_eight)
            inline_kb_full.row(reset_button, add_typing_button)
            return inline_kb_full

