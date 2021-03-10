from aiogram.dispatcher.filters.state import State, StatesGroup


class FreqNumberState(StatesGroup):
    number = State()