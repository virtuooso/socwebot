from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())