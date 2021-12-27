import os
from requests import get
from pyrogram import filters
from nksama import bot


@bot.on_message(filters.command('github'))
def git(_, message):
    user = message.text.split(' ')[1]
    res = get(f'https://api.github.com/users/{user}').json()
    data = f"""**Name**: {res['name']}
**UserName**: {res['login']}
**Link**: [{res['login']}]({res['html_url']})
**Bio**: {res['bio']}
**Company**: {res['company']}
**Location**: {res['location']}
**Public Repos: {res['public_repos']}
**Followers**: {res['followers']}
**Following**: {res['following']}
"""
    with open(f"{user}.jpg", "wb") as f:
        kek = get(res['avatar_url']).content
        f.write(kek)

    message.reply_photo(f"{user}.jpg", caption=data)
    os.remove(f"{user}.jpg")
