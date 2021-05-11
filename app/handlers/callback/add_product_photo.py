import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.misc import dp, bot
from app.states import FridgeProductState
from app.states.state_fridge_add_photo import FridgeAddPhotoState, FridgeAddPhotoCheckState
from app.states.state_shop_list_product import ShopListProductState
from app.states.state_shop_list_add_photo import ShoppingAddPhotoState, ShoppingAddPhotoCheckState
from app.keyboards.inline.add_product_method_photo import AddProductMethodChoice


@dp.callback_query_handler(filters.Text('add_product_photo_choice_[\'fridge\']'))
async def add_product_photo_choice_fridge_handler(query: types.CallbackQuery):
    info = re.findall(r'(fridge|shopping_list)', query.data)
    await bot.send_message(query.from_user.id,
                           "Что вы хотите сфотографировать?",
                           reply_markup=AddProductMethodChoice.create(info, query.message.message_id))
    await query.answer()


@dp.callback_query_handler(filters.Text('add_product_photo_choice_[\'shopping_list\']'))
async def add_product_photo_choice_shoplist_handler(query: types.CallbackQuery):
    info = re.findall(r'(fridge|shopping_list)', query.data)
    await bot.send_message(query.from_user.id,
                           "Что вы хотите сфотографировать?",
                           reply_markup=AddProductMethodChoice.create(info, query.message.message_id))
    await query.answer()


@dp.callback_query_handler(filters.Text('add_product_photo_check_[\'fridge\']'))
async def add_product_photo_check_fridge_handler(query: types.CallbackQuery):
    await FridgeAddPhotoCheckState.name.set()
    await bot.send_message(query.message.chat.id,
                           "Отправьте фото чека в хорошем качестве (без лишних предметов и надписей):")
    await query.answer()


@dp.callback_query_handler(filters.Text('add_product_photo_check_[\'shopping_list\']'))
async def add_product_photo_check_shoplist_handler(query: types.CallbackQuery):
    await ShoppingAddPhotoCheckState.name.set()
    await bot.send_message(query.message.chat.id,
                           "Отправьте фото чека в хорошем качестве (без лишних предметов и надписей):")
    await query.answer()


@dp.callback_query_handler(filters.Text('add_product_photo_[\'fridge\']'))
async def add_product_photo_fridge_handler(query: types.CallbackQuery):
    await FridgeAddPhotoState.name.set()
    await bot.send_message(query.message.chat.id,
                           "Отправьте фото продукта/этикетки в хорошем качестве (без лишних предметов и надписей):")
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'add_product_photo_name_ok_\[\'fridge\']\+.*'))
async def add_product_photo_fridge_nameok_handler(query: types.CallbackQuery, state: FSMContext):
    name = re.findall(r'[^+]*$', query.data)[0]
    async with state.proxy() as data:
        data['name'] = name
    await FridgeProductState.expiration_date.set()
    await bot.send_message(query.message.chat.id, 'Введите срок годности продукта ("дд.мм.гггг", пропустить - /skip)')
    await query.answer()


@dp.callback_query_handler(filters.Text('add_product_photo_[\'shopping_list\']'))
async def add_product_photo_shoplist_handler(query: types.CallbackQuery):
    await ShoppingAddPhotoState.name.set()
    await bot.send_message(query.message.chat.id,
                           "Отправьте фото продукта/этикетки в хорошем качестве (без лишних предметов и надписей):")
    await query.answer()


@dp.callback_query_handler(filters.Regexp(r'add_product_photo_name_ok_\[\'shopping_list\']\+.*'))
async def add_product_photo_shoplist_nameok_handler(query: types.CallbackQuery, state: FSMContext):
    name = re.findall(r'[^+]*$', query.data)[0]
    async with state.proxy() as data:
        data['name'] = name
    await ShopListProductState.info.set()
    await bot.send_message(query.message.chat.id, 'Введите дополнительную информацию о продукте ("дд.мм.гггг", пропустить - /skip)')
    await query.answer()

