from nksama import bot
from pyrogram import filters


@bot.on_message(filters.text & filters.chat(-1001544622735))
def nevermind(_,message):
  if message.from_user.id == 2080460107 and "completed" in message.text:
    message.delete()
