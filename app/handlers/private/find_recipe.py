from aiogram import types

from app.keyboards.inline.recipe_product_list_keyboard import RecipeProductListKeyboard
from app.misc import dp
from app.models import Product, ShoppingList, ShoppingListToProduct


@dp.message_handler(lambda message: message.text == 'Подобрать рецепт')
async def find_recipe_handler(msg: types.Message):
    products = await Product.query.where(Product.user_id == msg.from_user.id).gino.all()
    shopping_list_product_connections = await ShoppingList \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .select(ShoppingList.user_id == msg.from_user.id) \
        .gino.all()
    shopping_list_product_ids = [data[3] for data in shopping_list_product_connections]
    products = list(filter(lambda item: item.id not in shopping_list_product_ids, products))
    await msg.answer('Выберите продукты для поиска рецепта:',
                     reply_markup=RecipeProductListKeyboard.create(products, 0, 'recipe'))
