from nksama import bot
import os
from nksama.utils.sendlog import send_log
from pyrogram import filters


@bot.on_message(filters.command('rename'))
def rename(_, message):

    try:
        filename = message.text.replace(message.text.split(" ")[0], "")

    except Exception as e:
        send_log(e)

    if reply := message.reply_to_message:
        x = message.reply_text("Downloading.....")
        path = reply.download(file_name=filename)
        x.edit("Uploading.....")
        message.reply_document(path)
        os.remove(path)
