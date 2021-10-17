from requests import get
import random
from pyrogram import filters
from nksama import bot
import os


try:
  
  WALL_API_KEY = os.environ['WALL_API_KEY']
except:
  WALL_API_KEY = bot.get_messages(-1001646296281 , message_ids=370).text.split(":")[1] # api key from logs channel



class Wallpaper:
    def __init__(self , api_key , name) -> None:
        self.api_key = api_key
        self.name = name.replace(" " , "+")
        self.url = f"https://wall.alphacoders.com/api2.0/get.php?auth={self.api_key}&method=search&term={self.name}&width=1920&height=1080"


    def get_wallpaper(self):
        res = get(self.url).json()
        wallpapers = random.choice(res['wallpapers'])
        image , preview = wallpapers['url_image'] , wallpapers['url_thumb']
        return {"image": image , "preview": preview}




@bot.on_message(filters.command('wall'))
def wall(_,message):
    fk = Wallpaper(
        api_key=WALL_API_KEY,
        name = message.text.replace(message.text.split(" ")[0]  , "")
    )

    walll = fk.get_wallpaper()
    preview , image = walll['preview'] , walll['image']
    message.reply_photo(preview , caption="preview")
    message.reply_document(image)

