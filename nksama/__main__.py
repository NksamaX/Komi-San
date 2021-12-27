from nksama import bot, musicbot
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)


def main():
    bot().run()
    musicbot.start()
    bot.send_message(-1001544622735, "I'm Now online")


if __name__ == "__main__":
    main()
