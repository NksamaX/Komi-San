from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters
from pyrogram.types import Message
import requests
from nksama import help_message
from nksama.plugins.helpers import call_back_in_filter


@bot.on_callback_query(call_back_in_filter('meme'))
def callback_meme(_, query):
    if query.data.split(":")[1] == "next":
        query.message.delete()
        res = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
        img = res['image']
        title = res['title']
        bot.send_photo(
            query.message.chat.id,
            img,
            caption=title,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Next", callback_data="meme:next")],
            ]))


@bot.on_message(filters.command('rmeme'))
def rmeme(_, message):
    res = requests.get('https://nksamamemeapi.pythonanywhere.com').json()
    img = res['image']
    title = res['title']
    bot.send_photo(message.chat.id,
                   img,
                   caption=title,
                   reply_markup=InlineKeyboardMarkup([[
                       InlineKeyboardButton("Next", callback_data="meme:next")
                   ]]))


@bot.on_message(filters.command('webss'))
async def webss(client, message):
    user = message.command[1]
    fuck = f'https://webshot.deam.io/{url}/?delay=2000'
    await client.send_document(message.chat.id, fuck, caption=f'{url}')


help_message.append({"Module_Name": "meme"})
