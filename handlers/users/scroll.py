from loader import dp
from app import conn, cur

from aiogram.utils.exceptions import Throttled
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import types
from keyboard import menu


def update():
    global clans
    global checker

    cur.execute('SELECT * FROM clans;')

    groups = cur.fetchall()

    clans = iter(groups) if groups != [] else None
    checker = len(groups)
    

update()

@dp.message_handler(ChatTypeFilter(chat_type=types.ChatType.PRIVATE), text='Искать клан')
async def scroll(message: types.message):
    try:
        await dp.throttle('scroll', rate=3)
    except Throttled:
        await message.answer('Не спамь.')
    else:
        while clans != None:
            try:
                scrolling = next(clans)
                chat = await dp.bot.get_chat(scrolling[0])
            except StopIteration: 
                update()
            else:
                url = chat.invite_link

                if url == None:
                    cur.execute(f'DELETE FROM clans WHERE id={scrolling[0]};')
                    conn.commit()
                    continue
                elif chat.photo != None:
                    photo = await dp.bot.download_file_by_id(chat.photo.big_file_id)\
                     if await dp.bot.download_file_by_id(chat.photo.big_file_id) != None\
                        else await dp.bot.download_file_by_id(chat.photo.small_file_id)

                    await message.answer_photo(caption=f'''Название: {scrolling[1]}\n\nОписание: {scrolling[2]}\nСсылка: {url}''',\
                         photo=types.InputFile(photo), reply_markup=menu)

                    return
                else:
                    await message.answer(f'''Название: {scrolling[1]}\n\nОписание: {scrolling[2]}\nСсылка: {url}''',\
                         reply_markup=menu)
                         
                    return

        await message.answer('Нету групп!')
        return
                