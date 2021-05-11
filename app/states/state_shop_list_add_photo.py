from aiogram.dispatcher.filters.state import StatesGroup, State


class ShoppingAddPhotoState(StatesGroup):
    name = State()
    error = State()


class ShoppingAddPhotoCheckState(StatesGroup):
    name = State()
    error = State()