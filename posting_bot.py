import telegram
import imghdr
import random
import os
import time
import argparse
from environs import Env


def posting_bot():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_TOKEN"))
    parser = argparse.ArgumentParser(
        description="Укажите в часах с каким интервалом делать посты, по умолчанию - 4 часа"
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
            bot.send_photo(chat_id="-1002904882671", photo=open("images/" + file, "rb"))
            time.sleep(t)


def main():
    posting_bot()


if __name__ == "__main__":
    main()
