from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters 
from nksama import help_message

@bot.on_message(filters.command('start'))
def start(_,message):
    if chat.private:

        bot.send_message(message.chat.id , "Hello there i'm Komi-San\nI'll help you to manage your groups" , reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton('help' , callback_data="help")]
        ]))
   elif "help" in message.text:
     bot.send_message(message.chat.id , "Help" , reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton('help' , callback_data="help")]
   else:
         message.reply("Hello there i'm komi san")
