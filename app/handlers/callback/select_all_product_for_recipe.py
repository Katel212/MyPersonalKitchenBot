import re
from aiogram import types
from aiogram.dispatcher import filters, FSMContext

from app.models import Product, ShoppingList, ShoppingListToProduct

from app.misc import dp
from app.states.state_ingredients import IngredientsForRecipe


@dp.callback_query_handler(filters.Regexp(r'select_all_product_for_recipe'), state=IngredientsForRecipe.ingredients)
async def select_all_product_for_recipe(query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as st:
        name = re.match(r'select_all_product_for_recipe', query.data).groups()
        products = await Product.query.where(Product.user_id == query.from_user.id).gino.all()
        shopping_list_product_connections = await ShoppingList \
            .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
            .select(ShoppingList.user_id == query.from_user.id) \
            .gino.all()
        shopping_list_product_ids = [data[3] for data in shopping_list_product_connections]
        products = list(filter(lambda item: item.id not in shopping_list_product_ids, products))
        if len(st.get("ingredients", [])) == 0:
            st["ingredients"] = []
        for prod in products:
            st["ingredients"].append(prod.name)
    await query.answer()

