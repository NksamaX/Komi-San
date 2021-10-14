from pyrogram import filters , Client
import os 

bot = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['TOKEN'],
    plugins=dict(root=f"{__name__}/plugins")
)


help_message = []
