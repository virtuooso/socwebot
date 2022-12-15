from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
menu.add(KeyboardButton('Искать клан'), KeyboardButton('Помощь'))