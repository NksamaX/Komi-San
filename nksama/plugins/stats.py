from pyrogram import filters , Client
from nksama import bot
from pymongo import MongoClient 
from nksama.db import MONGO_URL as db_url

users_db = MongoClient(db_url)['users']
col = users_db['USER']


@bot.on_message(filters.command("stats"))
def stats(_,message):
  users = col.find({})
  mfs = []
  for x in users:
    mfs.append(x['user_id'])
    
  total = len(mfs)
  
  bot.send_message(message.chat.id , f"Total Users: {total}")
  


