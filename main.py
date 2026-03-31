import asyncio
from aiogram import Bot, Dispatcher

from secret.token import BOT_TOKEN
from bot.handlers.start import router

Bot_token = BOT_TOKEN

async def main():
    bot = Bot(token=Bot_token)
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())