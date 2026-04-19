import os
import logging
from threading import Thread
from web import app

# ---------------------------
# FLASK SERVER (SEPARATE)
# ---------------------------
def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)


# ---------------------------
# BOT START (ONLY ONCE)
# ---------------------------
def start_bot():
    try:
        import asyncio
        from src.app.main import main

        asyncio.run(main())

    except Exception as e:
        logging.exception(f"Bot failed to start: {e}")


# ---------------------------
# ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Flask in background
    Thread(target=run_flask, daemon=True).start()

    # Bot in main thread
    start_bot()
