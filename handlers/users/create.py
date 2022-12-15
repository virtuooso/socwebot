from aiogram import types
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import Throttled

from data import BOT_TOKEN
from app import cur, conn
from loader import dp


@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.GROUP), commands='create')
async def create(message: types.Message, command: Command.CommandObj):
    try:
        await dp.throttle('create', rate=60)
    except Throttled:
        await message.answer('Подожди минуту.')
    else:
        bot = await dp.bot.get_chat_member(message.chat.id, BOT_TOKEN.split(':')[0])
        user = await dp.bot.get_chat_member(message.chat.id, message.from_user.id)

        if bot.status == 'administrator' and user.status == 'creator':
            if command.args == None:
                cur.execute(f'SELECT EXISTS(SELECT * FROM clans WHERE id={message.chat.id});')

                if True in cur.fetchone():
                    cur.execute(f"UPDATE clans SET name = '{message.chat.title}' WHERE id = {message.chat.id};")
                    await message.answer('Вы успешно обновили имя клана.')
                else:
                    await message.answer('Пожалуйста, введите описание.')
            else:
                cur.execute(f'SELECT EXISTS(SELECT * FROM clans WHERE id={message.chat.id});')
                if True in cur.fetchone():
                    if len(command.args) <= 255:
                        cur.execute(f"UPDATE clans SET name = '{message.chat.title}', description = '{command.args}' WHERE id = {message.chat.id};")
                        await message.answer('Вы успешно обновили имя и описание клана.')
                    else:
                        await message.answer('Описание не больше 255 символов.')
                else:
                    if len(command.args) <= 255:
                        cur.execute(f"INSERT INTO clans VALUES({message.chat.id}, '{message.chat.title}', '{command.args}');")
                        await message.answer('Вы успешно зарегестрировали свой клан.')
        else:
            await message.answer('Вы или бот не имеют права выполнять эту команду.')
        
        conn.commit()
