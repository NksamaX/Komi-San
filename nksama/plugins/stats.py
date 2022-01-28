import os
import asyncio

from pyrogram import filters
from pyrogram.types import Message
from pymongo import MongoClient
from nksama import bot
from nksama.db import MONGO_URL as db_url

users_db = MongoClient(db_url)['users']
col = users_db['USER']
grps = users_db['GROUPS']


@bot.on_message(filters.command("stats"))
async def stats(_, m: Message):
    users = col.find({})
    mfs = [x['user_id'] for x in users]
    total = len(mfs)

    grp = grps.find({})
    grps_ = [x['chat_id'] for x in grp]
    total_ = len(grps_)

    await m.reply_text(f"👥 Total Users: `{total}`\n💭 Total Groups: `{total_}`")
