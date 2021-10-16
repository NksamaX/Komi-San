import re
import aiohttp
import requests
import asyncio


from pyrogram import filters
from time import time
from nksama import bot
from nksama.plugins.redis import kuki as r


BOT_ID = 2025517298

@bot.on_message(
    filters.command(["addchat", f"addchat@KomiSanRobot"])
)
async def addchat(_, m):
    is_kuki = r.is_kuki(int(m.chat.id))
    if not is_kuki:
        r.set_kuki(int(m.chat.id))
        m.reply_text(
            f"kuki AI Successfully {m.chat.id}"
        )
    await asyncio.sleep(5)

@bot.on_message(
    filters.command(["rmchat", f"rmchat@KomiSanRobot"])
)
async def rmchat(_, m):
    is_kuki = r.is_kuki(int(m.chat.id))
    if not is_kuki:
        r.rm_kuki(int(m.chat.id))
        m.reply_text(
            f" AI disabled successfully {m.chat.id}"
        )
    await asyncio.sleep(5)


@bot.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited
    & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def kuki(_, message):
    is_kuki = r.is_kuki(int(message.chat.id))
    if not is_kuki:
        return
    if not message.reply_to_message:
        return
    try:
        moe = message.reply_to_message.from_user.id
    except:
        return
    if moe != BOT_ID:
        return
    text = message.text
    Kuki = requests.get(f"https://www.kukiapi.xyz/api/apikey=KUKIwrLK87gL6/kuki/moezilla/message={text}").json()
    nksamax = f"{Kuki['reply']}"
    if "Komi" in text or "komi" in text or "KOMI" in text:
        await bot.send_chat_action(message.chat.id, "typing")
        await message.reply_text(nksamax)
