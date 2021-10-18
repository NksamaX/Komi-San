from nksama.db import MONGO_URL
import re
import aiohttp
import requests
import asyncio


from pyrogram import filters
from time import time
from nksama import bot


kuki = MONGO_URL.kuki


async def is_kuki(chat_id: int) -> bool:
    ai = await kuki.find_one({"chat_id": chat_id})
    if not ai:
        return False
    return True


async def set_kuki(chat_id: int):
    kukichat = await is_kuki(chat_id)
    if kukichat:
        return
    return await kuki.insert_one({"chat_id": chat_id})


async def rm_kuki(chat_id: int):
    kukichat = await is_kuki(chat_id)
    if not kukichat:
        return
    return await kuki.delete_one({"chat_id": chat_id})



BOT_ID = 2025517298

@bot.on_message(
    filters.command(["addchat", f"addchat@KomiSanRobot"])
)
async def addchat(_, message):
    chatk = message.chat.id
    if not await is_kuki(chatk):
        set_kuki(chatk)
        m.reply_text(
            f"kuki AI Successfully {message.chat.id}"
        )
    await asyncio.sleep(5)

@bot.on_message(
    filters.command(["rmchat", f"rmchat@KomiSanRobot"])
)
async def rmchat(_, message):
    chatk = message.chat.id
    if not await is_kuki(chatk):
        rm_kuki(chatk)
        m.reply_text(
            f" AI disabled successfully {message.chat.id}"
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
    try:
        chatk = message.chat.id
        if not await is_kuki(chatk):
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
    
    except Exception as e:
        await bot.send_message(-1001646296281 , f"error in chatbot:\n\n{e}")
