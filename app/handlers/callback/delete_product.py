import re

from aiogram import types
from aiogram.dispatcher import filters

from app.keyboards.inline.delete_product_keyboard import ConfirmDeleteProductKeyboard
from app.misc import dp, bot
from app.models import Product


def delete_product_confirm_message(name: str):
    return f'Вы действительно хотите удалить продукт "{name}"?'


@dp.callback_query_handler(filters.Regexp(r'delete_(\d+)'))
async def delete_confirm_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'delete_(\d*)', query.data).groups()
    product = await Product.query.where(Product.id == int(groups[0])).gino.first()

    await bot.send_message(query.from_user.id,
                           delete_product_confirm_message(product.name),
                           reply_markup=ConfirmDeleteProductKeyboard.create(product, query.message.message_id))


@dp.callback_query_handler(filters.Regexp(r'delete_yes_(\d+)_(\d+)'))
async def delete_yes_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'delete_yes_(\d+)_(\d+)', query.data).groups()

    await Product.delete.where(Product.id == int(groups[0])).gino.status()

    await bot.delete_message(query.message.chat.id, int(groups[1]))
    await query.message.delete()
    await bot.send_message(query.from_user.id, 'Продукт успешно удален')


@dp.callback_query_handler(filters.Regexp(r'delete_no_(\d+)'))
async def delete_no_callback_handler(query: types.CallbackQuery):
    await query.message.delete()
    await bot.send_message(query.from_user.id, 'Удаление продукта отменено')
