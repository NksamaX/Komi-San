from nksama import bot , musicbot
import logging




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.run()
    musicbot.start()
    with bot:
        bot.send_message(-1001544622735 , "I'm Now online")
    
