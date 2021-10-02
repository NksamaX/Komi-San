from re import escape
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from pyrogram.types.messages_and_media import message
from nksama import bot
from nksama.plugins.helpers import call_back_in_filter 

from pyrogram import filters
from nksama import help_message




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

        from pyrogram import filters 


@bot.on_callback_query(call_back_in_filter("admin"))
def admeme_callback(_,query):
    scammer = query.data.split(":")[2]
    if is_admin(query.message.chat.id , query.from_user.id) and query.data.split(":")[1] == "unban":
        bot.unban_chat_member(query.message.chat.id , scammer)
        query.answer('Unbanned!')
        query.message.edit(f'unbanned [{scammer}](tg://user?id={scammer})' , parse_mode='markdown')
    else:
        message.reply('You are not admin!')

@bot.on_message(filters.command('ban') & filters.command(f'ban@Dynasty_MangerBot'))
def ban(_,message):
    # scammer = reply.from_user.id
    reply = message.reply_to_message
    if is_admin(message.chat.id , message.from_user.id) and reply:
        bot.kick_chat_member(message.chat.id , message.reply_to_message.from_user.id)
        bot.send_message(message.chat.id ,f"Banned! {reply.from_user.username}" , parse_mode="markdown" ,reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Unban" , callback_data=f"admin:unban:{message.reply_to_message.from_user.id}")],
        ]))
    elif reply.from_user.id == 825664681:
        message.reply('This Person is my owner!')
    else:
        message.reply('You are not admin')


@bot.on_message(filters.command('unban') & filters.command(f'unban@Dynasty_MangerBot'))
def unban(_,message):
    try:
        user = message.text.split(" ")[1]
        if is_admin(message.chat.id , message.from_user.id):
            bot.unban_chat_member(message.chat.id , user)
            message.reply('Unbanned!')
    except Exception as e:
        message.reply(e)

    
@bot.on_message(filters.command('pin') & filters.command(f'pin@Dynasty_MangerBot'))
def pin(_,message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        if is_admin(message.chat.id , message.from_user.id): 
            bot.pin_chat_message(message.chat.id , message_id)
    
    elif not is_admin(message.chat.id , message.from_user.id): 
        message.reply("You're not admin")
    else:
        message.reply('Reply to a message')


@bot.on_message(filters.command('unpin') & filters.command(f'unpin@Dynasty_MangerBot'))
def pin(_,message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        if is_admin(message.chat.id , message.from_user.id): 
            bot.unpin_chat_message(message.chat.id , message_id)
    
    elif not is_admin(message.chat.id , message.from_user.id): 
        message.reply("You're not admin")
    else:
        message.reply('Reply to a message')

help_message.append({
    "Module_Name": "Admin" ,
    "Help": """
/ban - reply to a user
/unban user id or username
/pin - reply to a message
/unpin - reply to a message

"""})