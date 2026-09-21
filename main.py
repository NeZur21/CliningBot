import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handlers.start import router as start_router
from bot.handlers.order import router as order_router


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token='8877421496:AAE9yZW8_kSTaU1Jf1wMJeLMuJxLoDmxZpk')
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(order_router)

    await bot.delete_webhook(drop_pending_updates=True)

    print("Бот запущен")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())