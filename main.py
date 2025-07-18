import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router
from parsing import periodcheck

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot('')
    dp = Dispatcher()
    dp.include_router(router)
    try:
        asyncio.create_task(periodcheck(bot))
    except Exception as e:
        print(f"Ошибка в задаче: {e}")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
