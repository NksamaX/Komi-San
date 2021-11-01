from nksama import bot
from pyrogram import filters


CHAT = -1001552351131 
CHANNEL = -1001626853331 
kek = []


@bot.on_message(filters.media & filters.chat(CHAT))
def upload(_,message):
    if message.media:
        message.copy(CHANNEL)
        message.reply("Sent!")
