from pyrogram import filters
from nksama import bot , musicbot
import pytgcalls


calls = pytgcalls.GroupCallFactory(musicbot).get_group_call()


@bot.on_message(filters.command('play'))
async def play(_,message):
  reply = message.reply_to_message
  if reply:
    fk = await message.reply('Downloading....')
    path = await reply.download()
    await calls.join(message.chat.id)
    await calls.start_audio(path)
    await fk.edit('playing...')

    
@bot.on_message(filters.command('vplay'))
async def vplay(_,message):
  reply = message.reply_to_message
  if reply:
    path = reply.download()
    await calls.join(message.chat.id)
    await calls.start_video(path)
    await fk.edit('playing...')
