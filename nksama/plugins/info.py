from nksama import bot
from pyrogram import filters
from nksama.plugins.admin import sudos

OWNER = 825664681


@bot.on_message(filters.command("info"))
def info(_, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    if not message.reply_to_message and message.text != "/info" and user.isnumeric():
        user = message.text.split(" ")[1]
        
    if not message.reply_to_message and message.text != "/info" and not user.isnumeric():
        k = bot.get_users(user)
        user = k.id

    if user == OWNER:
        status = "This Person is my Owner"

    elif user in sudos:
        status = "This person is one of my Sudo users !"

    else:
        status = "member"

    pfp_count = bot.get_profile_photos_count(user)

    if not pfp_count == 0:
        pfp = bot.get_profile_photos(user, limit=1)
        pfp_ = pfp[0]['thumbs'][0]['file_id']

    foo = bot.get_users(user)
    data = f"""**First Name** : {foo.first_name}
**Last Name**: {foo.last_name}
**Telegram Id**: {foo.id}
**PermaLink**: {foo.mention(message.from_user.first_name)}
**is_bot**: {foo.is_bot}
**Status**: {status}
"""

    if pfp_count != 0:
        message.reply_photo(pfp_, caption=data)

    else:
        message.reply_text(data)
