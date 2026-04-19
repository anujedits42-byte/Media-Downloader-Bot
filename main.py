import asyncio
import os
from threading import Thread
from web import app

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

async def start_bot():
    from aiogram import Bot, Dispatcher

    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    # handlers yahan add karo

    await dp.start_polling(bot)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    asyncio.run(start_bot())
