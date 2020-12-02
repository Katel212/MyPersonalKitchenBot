from aiogram.dispatcher.filters.state import StatesGroup, State


class ShopListProductState(StatesGroup):
    name = State()
    info = State()
