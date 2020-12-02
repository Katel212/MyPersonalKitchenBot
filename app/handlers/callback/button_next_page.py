import re

from aiogram import types
from aiogram.dispatcher import filters
from loguru import logger

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.keyboards.inline.recipe_product_list_keyboard import RecipeProductListKeyboard
from app.misc import dp, bot
from app.models import Product


@dp.callback_query_handler(filters.Regexp(r'(previous_page|next_page)_(fridge|shopping_list|recipe)_(\d*)'))
async def page_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'(previous_page|next_page)_(fridge|shopping_list|recipe)_(\d*)', query.data).groups()
    new_page = 0
    if groups[0] == 'previous_page':
        new_page = int(groups[2]) - 1
    elif groups[0] == 'next_page':
        new_page = int(groups[2])+1
    source = groups[1]

    logger.info(f"Source: {source}")
    logger.info(f"Next page: {new_page}")

    keyboard = None
    products = None
    if source == 'fridge':
        products = await Product.query.where(Product.user_id == query.from_user.id).gino.all()
        keyboard = ProductListKeyboard.create(products, new_page, source)
    elif source == 'shopping_list':
        # TODO products=
        keyboard = ProductListKeyboard.create(products, new_page, source)
    elif source == 'recipe':
        products = await Product.query.where(Product.user_id == query.from_user.id).gino.all()
        keyboard = RecipeProductListKeyboard.create(products, new_page, source)
    await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id, reply_markup=keyboard)
    await query.answer()