from nksama.db import MONGO_URL as db_url
from nksama import bot
from pyrogram import filters
from nksama.plugins.admin import is_admin

profanity_db = pymongo.MongoClient(db_url)['Welcome']['WelcomeX']

@bot.on_message(filters.command("setprofanity"))
def toggle_profanity(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    x = message.text
    y = x.split(" ", 1)
    profanity_mode = y[1].lower
    if is_admin(chat_id , user_id):
        is_profanity = profanity_db.find_one({"chat_id": chat_id})

        if profanity_mode=="on":
            if is_profanity:
                return message.reply_text("Anti Profanity is already ON for this Chat")
            else:
                profanity_db.insert_one({"chat_id": chat_id})
                message.reply_text("Anti Profanity Turned on for this chat")

        elif profanity_mode=="off":
       	    if is_profanity:
                profanity_db.delete_one({"chat_id": chat_id})
                message.reply_text("Kay, Turned off Anti Profanity for This Chat")
            else:
                message.reply_text("Anti-Profanity is Already off For this Chat")    
    	else:
            message.reply_text("I accept on or off only")

    else:
        message.reply_text("You need to be Admin to execute this Command")

@bot.on_message(filters.text & filters.group)
def profanity(_, message):
    msg = message.text
    user_id = message.from_user.id
    chat_id = message.chat.id
    if is_admin(user_id, chat_id):
        return
    is_profanity = profanity_db.find_one({"chat_id": chat_id})
    if is_profanity:
        if msg in nksama.utils.profanity_words:
            try:
                message.delete()
                message.chat.restrict_member(
                    user_id,
                    ChatPermissions(),
                    until_date=(time() + 3600),
                )
                message.reply_text(f"Muted {message.from_user.mention} for 30 mins for saying Profanity Word")
            except:
                print("Some Error Occurred [Profanity]")
        else:
            return
    else:
        return
