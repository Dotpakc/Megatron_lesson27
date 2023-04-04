from aiogram.dispatcher.filters.state import State, StatesGroup

class RegForm(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    city = State()
    phone = State()