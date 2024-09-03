from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    waiting_for_day = State()
    waiting_for_name = State()
    waiting_for_confirm = State()
