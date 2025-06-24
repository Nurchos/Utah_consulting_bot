import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.start import router as start_router
from handlers.instructions import router as instructions_router
from handlers.notify import router as notify_router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Подключаем каждый router только один раз
    dp.include_router(start_router)
    dp.include_router(instructions_router)
    dp.include_router(notify_router)

    try:
        print("🤖 Бот запущен. Ожидание сообщений...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Бот остановлен с ошибкой: {e}")
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
