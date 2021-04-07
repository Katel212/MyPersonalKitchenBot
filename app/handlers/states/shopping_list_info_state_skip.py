from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.misc import dp
from app.models import Product, ShoppingList, ShoppingListToProduct
from app.states import ShopListProductState


@dp.message_handler(state=ShopListProductState.info,commands='skip')
async def handler_shopping_list_info_skip(msg: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    async with state.proxy() as data:
        data['info'] = None
        shop_list = await ShoppingList.query.where(ShoppingList.user_id == msg.from_user.id).gino.first()
        new_product = await Product.create(user_id=msg.from_user.id, name=data['name'], info=data['info'])
        await ShoppingListToProduct.create( product_id=new_product.id, shopping_list_id=shop_list.id)
        await msg.answer("Продукт успешно добавлен в ваш список покупок!")
    await state.finish()
