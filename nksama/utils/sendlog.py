from nksama import bot


def send_log(err , module):
   bot.send_message(-1001646296281 , f"error in {module}\n\n{err}")

   #.
