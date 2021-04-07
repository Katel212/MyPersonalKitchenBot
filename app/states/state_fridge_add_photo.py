from aiogram.dispatcher.filters.state import StatesGroup, State


class FridgeAddPhotoState(StatesGroup):
    name = State()
    error = State()