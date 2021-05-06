import os

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.keyboards.inline.add_product_photo import AddProductPhotoErrorShoppingList, AddProductPhotoGoodShoppingList,\
    AddProductPhotoCheckErrorShoplist, AddProductPhotoCheckGoodShoplist
from app.states import ShoppingAddPhotoState, ShoppingAddPhotoCheckState
from app import google_vision_recognizer
from app.misc import dp


@dp.message_handler(state=ShoppingAddPhotoState.name, content_types=['photo'])
async def handle_shopping_list_product_photo_state(msg: Message, state: FSMContext):
    f_name = google_vision_recognizer.generate_random_string(15) + '_rec.jpg'
    await msg.photo[-1].download(f_name)
    food_dict = google_vision_recognizer.load_food_names()
    foods = google_vision_recognizer.recognize_food(f_name, food_dict)
    os.remove(f_name)
    await state.finish()
    if len(foods) == 0:
        await msg.answer('Не удалось распознать продукт',
                         reply_markup=AddProductPhotoErrorShoppingList.create())
    else:
        await msg.answer('На фото изображено что-то из:',
                         reply_markup=AddProductPhotoGoodShoppingList.create(foods))


@dp.message_handler(state=ShoppingAddPhotoCheckState.name, content_types=['photo'])
async def handle_shopping_list_product_photo_state(msg: Message, state: FSMContext):
    f_name = google_vision_recognizer.generate_random_string(15) + '_rec.jpg'
    await msg.photo[-1].download(f_name)
    food_dict = google_vision_recognizer.load_food_names()
    foods = google_vision_recognizer.recognize_check(f_name, food_dict)
    os.remove(f_name)
    await state.finish()
    if len(foods) == 0:
        await msg.answer('Не удалось распознать чек',
                         reply_markup=AddProductPhotoCheckErrorShoplist.create())
    else:
        await msg.answer('На чек изображено что-то из:',
                         reply_markup=AddProductPhotoCheckGoodShoplist.create(foods))
