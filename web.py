import asyncio
from threading import Thread
from web import app
from pyrogram import idle
from bot import bot

# Flask run
def run_web():
    app.run(host="0.0.0.0", port=5000)

# Bot run
async def run_bot():
    await bot.start()
    print("Bot started ✅")
    await idle()
    await bot.stop()

# Start both
if __name__ == "__main__":
    Thread(target=run_web).start()
    asyncio.run(run_bot())
