from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from nksama import bot
from pyrogram import filters
import requests
from nksama import help_message
from nksama.plugins.helpers import call_back_in_filter


@bot.on_message(filters.command('pat'))
def pat(_, message):
    if reply := message.reply_to_message:
        res = requests.get('https://some-random-api.ml/animu/pat').json()
        url = res['link']
        reply.reply_animation(url)

    else:
        message.reply_animation(url)
