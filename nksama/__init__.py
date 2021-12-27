from pyrogram import filters, Client
from redis import Redis
import os
from nksama.plugins.help import Help_Text


help = Help_Text().helpp


help_message = []

class bot(Client):
  super().__init__(
    'bot',
     api_id=os.environ.get('API_ID'),
     api_hash=os.environ['API_HASH'],
     bot_token=os.environ['BOT_TOKEN'],
     plugins=dict(root=f"{__name__}/plugins")
  )
  
  def add_cmd(module , help):
    help_message.append({"Module_Name": module)
    help.update({f"{module}_help" : help})
                         

    
PYRO_SESSION = os.environ['PYRO_SESSION']

musicbot = Client(
    PYRO_SESSION,
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
)

