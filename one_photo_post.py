import telegram
import imghdr
import argparse
from environs import Env


def one_photo_post():
    
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env.str("TG_TOKEN"))
    parser = argparse.ArgumentParser(description="Публикация фото в канал")
    parser.add_argument(
        "--u",
        default="https://api.nasa.gov/assets/img/general/apod.jpg",
        help="Ссылка на фото для публикации",
    )
    args = parser.parse_args()
    url = args.u
    bot.send_photo(chat_id=env.str("TG_CHAT_ID"), photo=url)


def main():
    one_photo_post()


if __name__ == "__main__":
    main()
