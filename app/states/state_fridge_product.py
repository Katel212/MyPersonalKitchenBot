from aiogram.dispatcher.filters.state import StatesGroup, State


class FridgeProductState(StatesGroup):
    name = State()
    expiration_date = State()
    bought_date = State()
    info = State()
