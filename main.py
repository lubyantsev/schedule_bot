from aiogram import executor
from bot import dp
from handlers import register_handlers


def main():
    register_handlers(dp)  # Регистрация обработчиков
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
