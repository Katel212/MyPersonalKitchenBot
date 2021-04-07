from aiogram import types
from aiogram.dispatcher import filters

from app.misc import dp, bot
from app.states.state_fridge_product import FridgeProductState
from app.states.state_shop_list_product import ShopListProductState


@dp.callback_query_handler(filters.Text('add_product_typing_[\'fridge\']'))
async def add_product_typing_fridge_handler(query: types.CallbackQuery):
    await FridgeProductState.name.set()
    await bot.send_message(query.message.chat.id, "Введите название продукта:")
    await query.answer()

@dp.callback_query_handler(filters.Text('add_product_typing_[\'shopping_list\']'))
async def add_product_typing_shoplist_handler(query: types.CallbackQuery):
    await ShopListProductState.name.set()
    await bot.send_message(query.message.chat.id, "Введите название продукта:")
    await query.answer()

