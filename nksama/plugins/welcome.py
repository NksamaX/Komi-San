import pymongo
from nksama.db import MONGO_URL as db_url
from nksama import bot
from pyrogram import filters

welcome_db = pymongo.MongoClient(db_url)['Welcome']['WelcomeX']


@bot.on_message(filters.command('setwelcome'))
def setwelcome(_,message):
  all_welcome = welcome_db.find()
  if message.chat.id not in all_welcome:
    msg = message.text.replace(message.text.split(' ')[0] , "")
    welcome_db.insert_one({"type": "welcome" , "chat_id": message.chat.id , "welcome_text": msg})
    message.reply("Done!")
  else:
    message.reply("use /clearwelcome first!")

    
    
@bot.on_message(filters.command("clearwelcome"))
def clearwelcome(_,message):
  welcome_db.delete_one({"chat_id": message.chat.id})
  
 

@bot.on_message(filters.new_chat_members)
def welcome(_,message):
  try:
    welcome_msg = welcome_db.find_one({"chat_id" : message.chat.id})['welcome_text'] or ""
    if not welcome_msg == "":
      message.reply_text(welcome_msg)

    else:
      message.reply("Hello")
      
  except Exception as e:
    bot.send_message(-1001646296281 , f"error in welcome:\n]n{e}")
