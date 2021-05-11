import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from loguru import logger

from app.keyboards.inline.product_list_keyboard import ProductListKeyboard
from app.keyboards.inline.recipe_product_list_keyboard import RecipeProductListKeyboard
from app.misc import dp, bot
from app.models import Product, ShoppingList, ShoppingListToProduct, User
from app.states import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'(previous_page|next_page)_recipe_(\d*)'), state=IngredientsForRecipe.ingredients)
async def page_callback_handler(query: types.CallbackQuery, state: FSMContext):
    groups = re.match(r'(previous_page|next_page)_recipe_(\d*)', query.data).groups()
    new_page = 0
    if groups[0] == 'previous_page':
        new_page = int(groups[1]) - 1
    elif groups[0] == 'next_page':
        new_page = int(groups[1])+1

    logger.info(f"Next page: {new_page}")

    products = await Product.query.where(Product.user_id == query.from_user.id).gino.all()
    shopping_list_product_connections = await ShoppingList \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .select(ShoppingList.user_id == query.from_user.id) \
        .gino.all()
    shopping_list_product_ids = [data[3] for data in shopping_list_product_connections]
    products = list(filter(lambda item: item.id not in shopping_list_product_ids, products))
    keyboard = RecipeProductListKeyboard.create(products, new_page, 'recipe')
    await bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id, reply_markup=keyboard)
    await query.answer()