from aiogram.dispatcher.filters.state import State, StatesGroup


class DayOfWeekState(StatesGroup):
    name = State()