import logging
import os
from aiogram.filters import Command
from aiogram.types import Message

from app.data.config import get_log_level
from app.handlers import __modules__
from app.loader import dp, bot


logging.basicConfig(
    level=get_log_level(),  
    format="%(asctime)s - %(levelname)s - %(message)s",
)
log = logging.getLogger(__name__)

# Проверяем, есть ли загруженные модули
if not __modules__:
    log.warning("Нет загруженных модулей!")

# /ping
@dp.message(Command(commands=["ping"]))
async def ping(message: Message):
    log.info(f"Команда /ping от {message.from_user.id}") 
    await message.reply("Pong!")

def log_initialized_modules(modules: list = __modules__):
    log.info(f"Initialized modules: {[module.__name__ for module in modules]}")

# Entry point
if __name__ == '__main__':
    try:
        log_initialized_modules()
        log.info("Бот стартует...")

        dp.run_polling(bot) 
    except Exception as e:
        log.error(f"Ошибка запуска бота: {e}", exc_info=True)
