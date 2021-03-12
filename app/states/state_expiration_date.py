from aiogram.dispatcher.filters.state import State, StatesGroup


class ExpirationDateState(StatesGroup):
    number = State()