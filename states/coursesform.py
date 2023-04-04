from aiogram.dispatcher.filters.state import State, StatesGroup

class CourseForm(StatesGroup):
    select_course = State()
    info_course = State()

    