from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# 1. курси
# 2. Контакти
# 3. Про нас
# 4. Підтримка

main_kb = InlineKeyboardMarkup(row_width=2)
main_kb.add(InlineKeyboardButton(text='💻Курси', callback_data='courses'),
            InlineKeyboardButton(text='🛒Мерчь', callback_data='merch'),
            InlineKeyboardButton(text='📞Контакти', callback_data='contacts'),
            InlineKeyboardButton(text='📖Про нас', callback_data='about_us'),
            InlineKeyboardButton(text='💸Підтримка', callback_data='support'))
            