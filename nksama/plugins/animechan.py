import requests
from nksama import bot
from pyrogram import filters
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama.plugins.helpers import call_back_in_filter


@bot.on_callback_query(call_back_in_filter('quotek'))
def callback_quotek(_,query):
    if query.data.split(":")[1] == "change":
#         query.message.delete()
        kk = requests.get('https://animechan.vercel.app/api/random').json()
        anime = kk['anime']
        quote = kk['quote']
        character = kk['character']
        caption = f"""
**Anime:** `{anime}`
**Character:** `{character}`
**Quote:** `{quote}`"""
        query.message.edit(caption , reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Change" , callback_data="quotek:change")],
        ]))



@bot.on_message(filters.command('quote'))
def quote(_,message):
    kk = requests.get('https://animechan.vercel.app/api/random').json()
    anime = kk['anime']
    quote = kk['quote']
    character = kk['character']
    caption = f"""
**Anime:** `{anime}`
**Character:** `{character}`
**Quote:** `{quote}`"""
    bot.send_message(message.chat.id , caption , reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Change" , callback_data="quotek:change")]
    ]))


