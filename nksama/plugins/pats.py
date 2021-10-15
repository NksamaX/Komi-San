from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters
import requests
from nksama import help_message 
from nksama.plugins.helpers import call_back_in_filter


@bot.on_callback_query(call_back_in_filter('pat'))
def callback_pat(_,query):
    if query.data.split(":")[1] == "change":
        res = requests.get('https://some-random-api.ml/animu/pat').json()
        url = res['url']
        bot.send_photo(query.message.chat.id , url , reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Change" , callback_data="pat:change")],
        ]))



@bot.on_message(filters.command('pat'))
def pat(_,message):
    res = requests.get('https://some-random-api.ml/animu/pat').json()
    url = res['url']
    bot.send_photo(message.chat.id , img , reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Change" , callback_data="pat:change")]
    ]))


help_message.append(
    {
        "Module_Name": "Pat",
        "Help": "/pat - to get pat image"
    }
)
