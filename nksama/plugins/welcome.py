import pymongo
from nksama.db import MONGO_URL as db_url
from nksama import bot, help_message
from pyrogram import filters
from nksama.plugins.admin import is_admin

welcome_db = pymongo.MongoClient(db_url)['Welcome']['WelcomeX']


@bot.on_message(filters.command('setwelcome'))
def setwelcome(_, message):
    if is_admin(message.chat.id, message.from_user.id):
        try:
            ids = []
            all_welcome = welcome_db.find()
            for x in all_welcome:
                ids.append(x['chat_id'])

            if message.chat.id not in ids:
                msg = message.text.replace(message.text.split(' ')[0], "")
                welcome_db.insert_one({
                    "type": "welcome",
                    "chat_id": message.chat.id,
                    "welcome_text": msg
                })
                message.reply("Done!")
            else:
                message.reply("use /clearwelcome first!")

        except Exception as e:
            bot.send_message(-1001646296281, f"error in setwelcome:\n]n{e}")


@bot.on_message(filters.command("clearwelcome"))
def clearwelcome(_, message):
    if is_admin(message.chat.id, message.from_user.id):
        welcome_db.delete_many({"chat_id": message.chat.id})
        message.reply("Ok!")


@bot.on_message(filters.new_chat_members)
def welcome(_, message):
    try:
        welcome_msg = welcome_db.find_one({"chat_id": message.chat.id
                                           })['welcome_text'] or ""
        if not welcome_msg == "":
            message.reply_text(welcome_msg)

        else:
            message.reply("Hello")

    except Exception as e:
        bot.send_message(-1001646296281, f"error in welcome:\n]n{e}")


help_message.append({"Module_Name": "welcome"})
