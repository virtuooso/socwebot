from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter

from loader import dp

@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), text='Помощь')
async def help(message: types.Message):
    await message.answer('''Чтобы включить свою группу в наш список вам нужно:
    
1. Добавить бота в свою группу
2. Дать ему права администратора
3. Прописать команду /create с описанием в качестве аргумента 
    (Прим. /create Мой клан создан для тех, кто заинтересован в политике)
    
Так же вы можете обновить данные группы выполнив команду без аргумента ТОЛЬКО ПОСЛЕ РЕГИСТРАЦИИ. 
    
В этом случае вы обновите ТОЛЬКО имя своей группы. 
Если же вы напишите описание, то оно тоже будет обновлено.''')