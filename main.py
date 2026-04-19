import os
import asyncio
import logging
from threading import Thread
from web import app

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

async def start_bot():
    try:
        from src.app.main import main
        await main()
    except Exception as e:
        logging.exception(f"Bot failed to start: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    Thread(target=run_flask, daemon=True).start()
    asyncio.run(start_bot())
