# Komi-San
Telegram Group Management Bot based on Pyrogram

<b> More updates coming soon </b>

[Support Group](https://t.me/Komisan_Support)

<b> Open a Pull request
if you wana contribute </b>


Example for making new plugins

```
from nksama import bot , help_message
from pyrogram import filters

@bot.on_message(filters.command('hi'))
def hi(_,message):
  message.reply('hi')
  
help_message.append({"Module_Name": "hi" , "Help": "/hi - says hi"})

```
