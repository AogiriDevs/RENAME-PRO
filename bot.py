from pyrogram import Client
import os

TOKEN = os.environ.get("TOKEN", "5780840598:AAF50N-g14HT3xLSAe8K_Bmd5cLc562TYqU")

APP_ID = int(os.environ.get("APP_ID", "4665778"))

API_HASH = os.environ.get("API_HASH", "10e3ed833b0d09699973420d45359409")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "renamer",
        bot_token=TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
