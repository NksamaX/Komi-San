from requests import get
from pyrogram import filters, Client
from pyrogram.types import *
from bs4 import BeautifulSoup
from nksama import help_message
from nksama import bot


def call_back_in_filter(data):
    return filters.create(lambda flt, _, query: flt.data in query.data,
                          data=data)


@bot.on_callback_query(call_back_in_filter('fk'))
def fk(_, query):
    ani = None
    data = query.data.split(':')
    anime_id = data[1]
    url = f'https://chiaki.site/?/tools/watch_order/id/{anime_id}'
    res = get(url).text
    soup = BeautifulSoup(res, "html.parser")
    titles = soup.find_all('span', class_='wo_title')
    for x in titles:
        ani = f"{ani}\n{x}" if ani else x
    query.message.delete()
    query.message.reply(f'**Results for {anime_}**\n\n```{ani}```')


@bot.on_message(filters.command('watchorder'))
def watchorder(_, message):
    global anime_
    anime_ = message.text.replace(message.text.split(' ')[0], '')
    res = get(f'https://chiaki.site/?/tools/autocomplete_series&term={anime_}'
              ).json()
    keyboard = [[
        InlineKeyboardButton(x['value'], callback_data="fk:{}".format(x['id']))
    ] for x in res]
    bot.send_message(message.chat.id,
                     "results for {}".format(anime_),
                     reply_markup=InlineKeyboardMarkup(keyboard))


help_message.append({"Module_Name": "extra"})
