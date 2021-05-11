from aiogram import types
from aiogram.dispatcher import FSMContext

from app.keyboards.inline.recipe_product_list_keyboard import RecipeProductListKeyboard
from app.misc import dp
from app.models import Product, ShoppingList, ShoppingListToProduct
from app.states import IngredientsForRecipe


@dp.message_handler(lambda message: message.text == 'Подобрать рецепт')
async def find_recipe_handler(msg: types.Message):

    products = await Product.query.where(Product.user_id == msg.from_user.id).gino.all()
    shopping_list_product_connections = await ShoppingList \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .select(ShoppingList.user_id == msg.from_user.id) \
        .gino.all()
    shopping_list_product_ids = [data[3] for data in shopping_list_product_connections]
    products = list(filter(lambda item: item.id not in shopping_list_product_ids, products))
    await IngredientsForRecipe.ingredients.set()
    await msg.answer('Выберите продукты для поиска рецепта:', reply_markup=RecipeProductListKeyboard.create(products, 0, 'recipe'))


@dp.message_handler(lambda message: message.text == 'Подобрать рецепт',state='*')
async def find_recipe_handler_st(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    products = await Product.query.where(Product.user_id == msg.from_user.id).gino.all()
    shopping_list_product_connections = await ShoppingList \
        .join(ShoppingListToProduct, ShoppingListToProduct.shopping_list_id == ShoppingList.id) \
        .select(ShoppingList.user_id == msg.from_user.id) \
        .gino.all()
    shopping_list_product_ids = [data[3] for data in shopping_list_product_connections]
    products = list(filter(lambda item: item.id not in shopping_list_product_ids, products))
    await IngredientsForRecipe.ingredients.set()
    await IngredientsForRecipe.next()
    async with state.proxy() as kcal:
        kcal['kcal'] = None
    await IngredientsForRecipe.previous()
    await msg.answer('Выберите продукты для поиска рецепта:', reply_markup=RecipeProductListKeyboard.create(products, 0, 'recipe'))
