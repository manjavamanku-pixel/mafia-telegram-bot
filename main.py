import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
import database as db
from handlers import start

async def main():
    # Xatoliklarni ko'rish uchun loglarni yoqish
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    
    # Ma'lumotlar bazasini (PostgreSQL) ishga tushirish
    await db.init_db()
    
    # Botni ulash
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    
    # Start menyusini (router) botga qoshish
    dp.include_router(start.router)
    
    logging.info("Bot ishga tushdi!")
    
    # Eski xabarlarni o'qib qotib qolmasligi uchun
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
