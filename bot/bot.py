import os
import pyrogram

from bot import API_HASH, TG_BOT_TOKEN, APP_ID 

if __name__ == "__main__":
    plugins = dict(
        root="bot/plugins"
    )
    app = pyrogram.Client(
        "copybot",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )

    app.run
