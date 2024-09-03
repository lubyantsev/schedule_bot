import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = 'tkn'  # Замените на ваш токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token='tkn')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
