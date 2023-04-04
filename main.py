import logging

async def on_startup(dp):
    from utils import load_users
    from loader import bot
    users = load_users()
    try:
        for user in users:
            await bot.send_message(user['id'], 'Бот запущено')
            await bot.send_message(user['id'], f'Ваші дані: {user}\n Якщо ви хочете змінити дані, використовуйте команду /reg')
    except Exception as e:
        logging.exception(e)
    print('BOT ONLINE')
    


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_polling(dp, skip_updates=True)
    