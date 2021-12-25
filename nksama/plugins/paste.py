from requests import post , get
from nksama import bot
from pyrogram import filters


def paste(text):
  url = "https://spaceb.in/api/v1/documents/"
  res = post(url , data={"content": text , "extension":"txt"})
  return f"https://spaceb.in/{res.json()['payload']['id']}"

  
@bot.on_message(filters.command('paste'))
def pastex(_,message):
  text = message.reply_to_message
  if text:
    x = paste(text.text)
    message.reply(x)
    
  else:
    message.reply_text("Reply to a message!")
