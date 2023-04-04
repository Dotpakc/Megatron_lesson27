from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from utils import load_users
from states.regformst import RegForm
from keyboards.main_kb import main_kb


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    users = load_users()
    user_id = message.from_user.id
    if user_id not in [user['id'] for user in users]:
        await RegForm.first_name.set()
        await message.answer("Привіт, як тебе звати?")
        return
    
    await message.answer("Привіт, я бот)))", reply_markup = main_kb)


@dp.message_handler(commands=['lol'])
async def lol_answer(message: types.Message):
    await message.answer('Прикол, і ти знаєш, що це за прикол?')
    

@dp.callback_query_handler(text='contacts')
async def process_callback_button1(call: types.CallbackQuery):
    if call.message.text.startswith('Зателефонуй'):
        await call.answer('ви вже викликали контакти')
        return
    text = 'Зателефонуй нам за номером: +380000000000\n Або напиши нам на пошту: school@ii.ua'
    await call.message.edit_text(text=text, reply_markup=main_kb)