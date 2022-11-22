from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text="Bot succesfuliy started!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "⭕️ JOIN OUR CHANNEL ⭕️", url="https://t.me/DFF_UPDATES")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
