from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class OtherSettingsListKeyboard(InlineKeyboardMarkup):
    @staticmethod
    def create():
        default_list_of_products_button = InlineKeyboardButton('Загрузить дефолтный список продуктов',
                                                               callback_data=f'other_default_list_of_products')
        automatically_set_the_purchase_date_button = InlineKeyboardButton('Автоматически проставлять дату покупки',
                                                                          callback_data=f'other_auto_set_purchase_date')

        return InlineKeyboardMarkup(
            inline_keyboard=[[default_list_of_products_button], [automatically_set_the_purchase_date_button]

                             ])
