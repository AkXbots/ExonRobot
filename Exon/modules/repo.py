# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi1M
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Exon import Abishnoi as pbot

ABISHNOIX = "https://te.legra.ph/file/abfc49a1cc4b5629dc8cd.jpg"


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=ABISHNOIX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ᴏᴡɴᴇʀ  : [Zeus Xd Afk](https://t.me/Zeus_Xd_Afk)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
** ᴇɴᴊᴏʏ**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴍᴜꜱɪᴄ•", url="https://t.me/Lucci_Music_bot"
                    ),
                    InlineKeyboardButton(
                        "•ʀᴏʙᴏᴠ1•", url="https://youtu.be/oCuw7zDOQlI"
                    ),
                ]
            ]
        ),
    )
