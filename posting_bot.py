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
        description="Скрипт загружает изображение в телеграм-канал с заданной периодичностью"
    )
    parser.add_argument(
        "--t", default=4, help="длительность интервала постинга в часах (по умолчанию - 4)"
    )
    args = parser.parse_args()

    posting_interval_hours = int(args.t)*3600
    filenames = os.listdir("images/")
    while filenames:
        random.shuffle(filenames)
        for file in filenames:
            with open(f"images/{file}", "rb") as photo:
                bot.send_photo(chat_id=env.str("TG_CHAT_ID"), photo=photo)
            time.sleep(posting_interval_hours)


def main():
    post_image_tg_bot()


if __name__ == "__main__":
    main()
