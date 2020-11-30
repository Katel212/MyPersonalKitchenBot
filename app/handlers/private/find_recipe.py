from aiogram import types

from app.keyboards.inline.recipe_product_list_keyboard import RecipeProductListKeyboard
from app.misc import dp
from app.models import Product


@dp.message_handler(lambda message: message.text == 'Подобрать рецепт')
async def find_recipe_handler(msg: types.Message):
    products = await Product.query.where(Product.user_id == msg.from_user.id).gino.all()
    await msg.answer('Выберите продукты для поиска рецепта:', reply_markup=RecipeProductListKeyboard.create(products, 0, 'recipe'))
