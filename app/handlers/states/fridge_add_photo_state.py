import os

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.keyboards.inline.add_product_photo import AddProductPhotoErrorFridge, AddProductPhotoGoodFridge
from app.states import FridgeAddPhotoState
from app import google_vision_recognizer
from app.misc import dp



@dp.message_handler(state=FridgeAddPhotoState.name, content_types=['photo'])
async def handle_fridge_product_photo_state(msg: Message, state: FSMContext):
    f_name = google_vision_recognizer.generate_random_string(15) + '_rec.jpg'
    await msg.photo[-1].download(f_name)
    food_dict = google_vision_recognizer.load_food_names()
    food = google_vision_recognizer.recognize_food(f_name, food_dict)
    os.remove(f_name)
    await state.finish()
    if food == 'Not_Found':
        await msg.answer('Не удалось распознать продукт',
                         reply_markup=AddProductPhotoErrorFridge.create())
    else:
        await msg.answer('На фото изображено: ' + food + '\nВсё верно, добавлять?',
                         reply_markup=AddProductPhotoGoodFridge.create(food))
