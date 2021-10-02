
from nksama import bot , help_message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton , InlineKeyboardMarkup

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

    for x in help_message:
            global helptext_
            helptext_ = x['Help']
        
    if not query.data == "help":
        msg = query.message
        module = query.data.split(':')[1]
        txt =  helptext_

        msg.edit(txt)
    
    elif query.data == "help":
        
            query.message.edit("Commands and help" , reply_markup=InlineKeyboardMarkup([ 
                [InlineKeyboardButton(x['Module_Name'], callback_data=f"help:{x['Module_Name']}")],
            ]))


    
    
