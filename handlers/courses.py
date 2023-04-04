import os
import json

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
# from utils import load_users
from states.coursesform import CourseForm
from keyboards.main_kb import main_kb


def get_course_kb():
    list_of_courses_dir = os.listdir('shop/course')
    course_kb = types.InlineKeyboardMarkup(row_width=2)
    for course in list_of_courses_dir:
        course_kb.add(types.InlineKeyboardButton(text=course, callback_data=course))
    return course_kb


def get_course_info(course):
    file_list = os.listdir(f'shop/course/{course}')
    file_json = [file for file in file_list if file.endswith('.json')][0]
    with open(f'shop/course/{course}/{file_json}', 'r', encoding='utf-8') as file:
        course_info = json.load(file)
    return course_info

def get_course_photo(course):
    file_list = os.listdir(f'shop/course/{course}/img')
    file_photo = [file for file in file_list][0]
    with open(f'shop/course/{course}/img/{file_photo}', 'rb') as file:
        photo = file.read()
    return photo


@dp.callback_query_handler(text='courses')
async def process_callback_button1(call: types.CallbackQuery):
        course_kb = get_course_kb()
        text = 'Виберіть курс'
        await CourseForm.select_course.set()
        await call.message.edit_text(text=text, reply_markup=course_kb)

@dp.callback_query_handler(state=CourseForm.select_course)
async def select_courses(call: types.CallbackQuery, state: FSMContext):
    course = call.data
    course_info = get_course_info(course)
    text = f'Назва курсу: {course_info["name"]}\nОпис: {course_info["description"]}\nЦіна: {course_info["prices"]}'
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text='Купити', url=course_info['link']))
    markup.add(types.InlineKeyboardButton(text='Назад', callback_data='courses_back'))
    photo = get_course_photo(course)
    await call.message.answer_photo(photo=photo, caption=text, reply_markup=markup)
    await call.message.delete()
    await CourseForm.next()
    
@dp.callback_query_handler(text='courses_back', state=CourseForm.info_course)
async def process_callback_button1(call: types.CallbackQuery):
    course_kb = get_course_kb()
    text = 'Виберіть курс'
    await CourseForm.select_course.set()
    await call.message.answer(text=text, reply_markup=course_kb)
    await call.message.delete()