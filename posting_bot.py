import telegram
import imghdr
import random
import os
import time
import argparse
from environs import Env


def post_image_tg_bot():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_TOKEN"))
    parser = argparse.ArgumentParser(
        description="Скрипт загружает изобращение в телеграм-канал с заданной периодичностью"
    )
    parser.add_argument(
        "--t", default=4, help="длительность интервала постинга (в часах)"
    )
    args = parser.parse_args()

    t = int(args.t)*3600
    files = os.listdir("images/")
    while files:
        random.shuffle(files)
        for file in files:
            bot.send_photo(chat_id=env.str("TG_CHAT_ID"), photo=open("images/" + file, "rb"))
            time.sleep(t)


def main():
    post_image_tg_bot()


if __name__ == "__main__":
    main()
