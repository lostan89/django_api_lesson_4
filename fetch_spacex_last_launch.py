import requests
import argparse
from additional import save_image_to_path


def fetch_spacex_last_launch(launch_id):
        api_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
        response = requests.get(api_url)
        response.raise_for_status()
        spacex_photos = response.json()
        image_urls = spacex_photos["links"]["flickr"]["original"]
        return image_urls


def main():
    parser = argparse.ArgumentParser(
        description="Программа сохраняет фото с запуска SpaceX, по умолчанию с последнего"
    )
    parser.add_argument("--id", help="Введите ID запуска, фото с которого Вы хотите сохранить", default="latest")
    args = parser.parse_args()
    image_urls = fetch_spacex_last_launch(args.id)
    if image_urls:
        for image_number, image_url in enumerate(image_urls):
            try:
                save_image_to_path(f"spacex_{str(image_number)}", image_url, "images/")
            except requests.exceptions.HTTPError:
                print("Такой ID полета не существует")
        else:
            print("Фотографии с последнего запуска отсутствуют")


if __name__ == "__main__":
    main()
