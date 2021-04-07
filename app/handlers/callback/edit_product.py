import datetime
import re

from aiogram import types
from aiogram.dispatcher import filters

from app.handlers.states.change.change_name_state import ChangeProductState
from app.keyboards.inline.edit_product_keyboard import ChangeInfoAboutProductKeyboard
from app.misc import dp, bot
from app.models import Product


def edit_info_product_message(name: str, exp_date: datetime, bought_date: datetime, info: str):
    bubble = f'Продукт:\n{name}\n'
    if exp_date is not None:
        bubble += f'Срок годности: до {exp_date}\n'
    if bought_date is not None:
        bubble += f'Дата покупки: {bought_date}\n'
    bubble += info if info else ''
    bubble+='Что изменить?'
    return bubble


@dp.callback_query_handler(filters.Regexp(r'change_(\d+)'))
async def edit_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'change_(\d*)', query.data).groups()
    product = await Product.query.where(Product.id == int(groups[0])).gino.first()
    await bot.send_message(query.from_user.id,
                           "Что изменить?",
                           reply_markup=ChangeInfoAboutProductKeyboard.create(product))


@dp.callback_query_handler(filters.Regexp(r'change_name_(\d+)'))
async def change_name_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'change_name_(\d+)', query.data).groups()
    ChangeProductState.id = groups[0]
    await bot.send_message(query.message.chat.id, "Введите новое название продукта (пропустить - /skip):")
    await ChangeProductState.name.set()


@dp.callback_query_handler(filters.Regexp(r'change_expiration_date_(\d+)'))
async def change_expiration_date_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'change_expiration_date_(\d+)', query.data).groups()
    ChangeProductState.id = groups[0]
    await bot.send_message(query.message.chat.id,
                           "Введите новую дату истечения срока годности(дд.мм.гггг, пропустить - /skip):")
    await ChangeProductState.expiration_date.set()


@dp.callback_query_handler(filters.Regexp(r'change_bought_time_(\d+)'))
async def change_bought_time_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'change_bought_time_(\d+)', query.data).groups()
    ChangeProductState.id = groups[0]
    await bot.send_message(query.message.chat.id, "Введите новую дату покупки (дд.мм.гггг, пропустить - /skip):")
    await ChangeProductState.bought_date.set()


@dp.callback_query_handler(filters.Regexp(r'change_info_(\d+)'))
async def change_info_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'change_info_(\d+)', query.data).groups()
    ChangeProductState.id = groups[0]
    await bot.send_message(query.message.chat.id, "Введите новую информацию о продукте (пропустить - /skip):")
    await ChangeProductState.info.set()
