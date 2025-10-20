import requests
import argparse
import sys
from additional import save_image_to_path


def fetch_spacex_last_launch(launch_id):
    if launch_id:
        api_url = "https://api.spacexdata.com/v5/launches/" + launch_id
    else:
        api_url = "https://api.spacexdata.com/v5/launches/latest"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        spacex_photo = response.json()
        url_image = spacex_photo["links"]["flickr"]["original"]
        return url_image
    except requests.exceptions.HTTPError:
        print("Такой ID полета не существует")
        sys.exit()


def main():
    parser = argparse.ArgumentParser(
        description="Введите ID запуска или пропустите, для показа фото с последнего запуска"
    )
    parser.add_argument("--id", help="ID запуска")
    args = parser.parse_args()
    print(fetch_spacex_last_launch(args.id))
    if fetch_spacex_last_launch(args.id):
        for image_number, image_url in enumerate(fetch_spacex_last_launch(args.id)):
            save_image_to_path("spacex_" + str(image_number), image_url, "images/")
    else:
        print("Фотографии с последнего запуска отсутствуют")


if __name__ == "__main__":
    main()
