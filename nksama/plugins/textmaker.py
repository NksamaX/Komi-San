from pyrogram import filters

from nksama import bot

@bot.on_message(filters.command("plat"))
async def plat(_,message):
    try:
        user = message.command[1]
        await message.delete()
        url = f"https://gdcolon.com/tools/gdlogo/img/{text}"
        await bot.send_document(message.chat.id, url, caption=f"{text}")
