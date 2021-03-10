import re

from aiogram import types
from aiogram.dispatcher import filters

from app.misc import dp, bot
from app.states.state_fridge_product import FridgeProductState
from app.states.state_shop_list_product import ShopListProductState


@dp.callback_query_handler(filters.Regexp(r'add_to_(fridge|shopping_list)'))
async def add_to_callback_handler(query: types.CallbackQuery):
    groups = re.match(r'add_to_(fridge|shopping_list)', query.data).groups()
    source = groups[0]
    if source == 'fridge':
        await FridgeProductState.name.set()
    elif source == 'shopping_list':
        await ShopListProductState.name.set()

    await bot.send_message(query.message.chat.id, "Введите название продукта")
    await query.answer()
