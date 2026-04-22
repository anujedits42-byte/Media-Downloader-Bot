import asyncio
from threading import Thread
from web import app

# 👇 tumhara aiogram bot main function
from src.app.main import main


# Flask run
def run_flask():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    # Flask ko background me chalao
    Thread(target=run_flask, daemon=True).start()

    # Bot start karo
    asyncio.run(main())
