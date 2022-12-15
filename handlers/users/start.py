from loader import dp
from aiogram import types
from keyboard import menu

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Добро пожаловать. Вы используете бота, который связывает разные объединения людей в одном месте!', reply_markup=menu)