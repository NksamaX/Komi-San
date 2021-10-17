from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters 
from nksama import help_message

group_id = 1544622735

@bot.on_message(filters.command('start') & filters.chat(group_id))
def start(_,message):

    bot.send_message(message.chat.id , "Hello there i'm Komi-San\nI'll help you to manage your groups" , reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('help' , callback_data="help")]
    ]))
