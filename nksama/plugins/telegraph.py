
from telegraph import upload_file
from pyrogram import filters
from nksama import bot


@bot.on_message(filters.command('ul'))
def ul(_,message):
    reply = message.reply_to_message
    if reply.media:
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x
        
        message.reply_text(f'Your telegraph [link]({url})',disable_web_page_preview=True)


