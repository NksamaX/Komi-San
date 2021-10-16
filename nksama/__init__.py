from pyrogram import filters , Client
from redis import StrictRedis
import os 

bot = Client(
    'bot',
    REDIS_URI = os.environ.get("REDIS_URI"),
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    plugins=dict(root=f"{__name__}/plugins")
)

REDIS_URI = os.environ.get("REDIS_URL")

REDIS_DB = StrictRedis.from_url(REDIS_URI
                                ,decode_responses=True
                               )

REDIS_DB.ping()




help_message = []
