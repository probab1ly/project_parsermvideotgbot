import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router
from parsing import periodcheck

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot('8198291115:AAFwKUlXZll4_f0GmN-EMGAS-jsrvHVPrPc')
    dp = Dispatcher()
    dp.include_router(router)
    asyncio.create_task(periodcheck(bot))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
