
from os import name
from pyrogram.methods import messages
from nksama import bot , help_message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup
from nksama.plugins.helptext import Help_Text


fk = Help_Text()

def call_back_in_filter(data):
    return filters.create(
        lambda flt, _, query: flt.data in query.data,
        data=data
    )


def is_admin(group_id: int, user_id: int):
    try:
        user_data = bot.get_chat_member(group_id, user_id)
        if user_data.status == 'administrator' or user_data.status == 'creator':
            # print(f'is admin user_data : {user_data}')
            return True
        else:
            # print('Not admin')
            return False
    except:
        # print('Not admin')
        return False

       



@bot.on_callback_query(call_back_in_filter('help'))
def callback_help(_,query):
        
    if not query.data == "help":
        try:
            for x in help_message:
                module = query.data.split(':')[1]
                module_name = f'{module}_help'
                query.message.edit(fk.helpp.get(module_name) , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back" , callback_data="help:back")]]))
           
            msg = query.message
            callback_module_name = query.data.split(':')[1]
            txt =  helptext_

            query.message.edit(txt)
        except Exception as e:
            bot.send_message(-1001646296281 , f"error in help:\n\n{e}")
    
    if query.data == "help":
        keyboard = []
        for x in help_message:
            keyboard.append([InlineKeyboardButton(x['Module_Name'], callback_data=f"help:{x['Module_Name']}")])

        query.message.edit("Commands and Help" , reply_markup=InlineKeyboardMarkup(keyboard))
        
    if query.data.split(":")[1] == "back":
        keyboard = []
        for x in help_message:
            keyboard.append([InlineKeyboardButton(x['Module_Name'], callback_data=f"help:{x['Module_Name']}")])
        query.message.edit("commands and help" , reply_markup=InlineKeyboardMarkup(keyboard))
            


    
    
