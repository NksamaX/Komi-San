from nksama.db import database as db
from nksama import bot
from pyrogram import filters
import json
from nksama import help_message

@bot.on_message(filters.command('addnote'))
def addnote(_,message):
    note = message.text.split(' ')[1]
    text = message.text.replace(message.text.split(" ")[0] , "").replace(message.text.split(' ')[1] , "")
    db.insert_one(
        {
            "type": "note",
            "chat_id": message.chat.id,
            "note_name": note,
            "text": text
        }
    )

    message.reply_text('Added!')


@bot.on_message(filters.command('getnote'))
def get_note(_,message):
    try:
        note = message.text.split(' ')[1]
        data = db.find_one({"chat_id": message.chat.id , "type": "note" , "note_name": note})
        message.reply(data['text'])
        
        
    except Exception as e:
        message.reply(e)
        
   
@bot.on_message(filters.regex(r"^#.+"))
def gettnote(_,message):
    try:
        note_name = message.text.replace("#" , "")
        data = db.find_one({"chat_id": message.chat.id , "type": "note" , "note_name": note_name})
        message.reply(data['text'])
    
    except Exception as e:
        message.reply(e)
        
    

@bot.on_message(filters.command('notes'))
def notes(_,message):
    notes = None

    # if notes:
    #     for x in db.find({"chat_id": message.chat.id}):
    #         notes = f"{notes}\n{x}"
    #         message.reply(notes)
    # else:
    #     for x in db.find({"chat_id": message.chat.id}):
    #         notes = x

    for x in db.find({"chat_id": message.chat.id}):
        if notes:
            notes = f"{notes}\n{x['note_name']}"
        
        else:
            notes = x['note_name']
    
    message.reply(notes)

    

@bot.on_message(filters.command('delnote'))
def delnote(_,message):
    note = message.text.split(" ")[1]
    db.delete_one({"note_name": note})
    message.reply('Deleted!')
    
    
    


help_message.append({
    "Module_Name": "notes",
    "Notes_Help": "/addnote note name text - to add a note\n/delnote NoteName - to delete a note\ngetnote NoteName - get a note\n/notes - to get a list of notes in your chats"
})
