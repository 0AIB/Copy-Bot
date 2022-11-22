import os
import time
from bot import CHANNEL_ID

from pyrogram.errors import FloodWait
from pyrogram import Client, filters


@Client.on_message(filters.media)
async def forward(bot, update):
    try:
        await bot.copy_message(
            chat_id=CHANNEL_ID,
            from_chat_id=update.chat.id,
            message_id=update.message_id,
            caption=update.caption
        )
    except FloodWait as e:
        time.sleep(e.x)

