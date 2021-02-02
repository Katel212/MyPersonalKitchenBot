from aiogram.dispatcher.filters.state import State, StatesGroup


class ChangeProductState(StatesGroup):
    id = int()
    name = State()
    expiration_date = State()
    bought_date = State()
    info = State()
