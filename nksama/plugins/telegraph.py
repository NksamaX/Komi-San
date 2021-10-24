import requests
from PIL import Image
from nksama import bot
import os
from pyrogram import filters

@bot.on_message(filters.command('ul'))
def ul(_,message):
   if message.reply_to_message.media:
        path = message.reply_to_message.download()
        file = {
            ("media", open(path, 'rb'))
        }

        res = requests.post("https://telegra.ph/upload" , files=file)

        for x in res.json():
            if not "webp" in path:
                link = x['src']
                bot.send_message(message.chat.id , f"https://telegra.ph{link})")
                os.remove(path)
            else:
                sticker = Image.open(path).convert("RGB")
                sticker.save(f"{path}.jpg" , "jpeg")
                file = {
                    ("media", open(f"{path}.jpg" , 'rb'))
                }
                res = requests.post("https://telegra.ph/upload" , files=file)
                print(res.text)
                for x in res.json():
                    link = x['src']
                    bot.send_message(message.chat.id , f"https://telegra.ph{link}")
                    os.remove(f"{path}.jpg")
