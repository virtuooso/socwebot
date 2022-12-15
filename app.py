import psycopg2

conn = psycopg2.connect('dbname=bainda user=postgres password=postgres')
cur = conn.cursor()

async def on_startup(dp):
    print('Бот запущен.')
    
async def on_shutdown(dp):
    print('Бот выключен.')
    conn.commit()

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)