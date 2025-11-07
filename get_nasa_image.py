import requests
from environs import Env
from additional import save_image_to_path


def get_nasa_images(api_key, count):
    api_url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": api_key, "count": count}
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    nasa_photos = response.json()
    image_urls = []
    for image in nasa_photos:
        url = image.get("url")
        if url:
            image_urls.append(url)
    return image_urls


def main():
    env = Env()
    env.read_env()
    api_key = env.str("NASA_API_KEY")
    count_of_images = 30
    nasa_images = get_nasa_images(api_key, count_of_images)
    for image_number, image_url in enumerate(nasa_image):
        save_image_to_path(f"nasa_apod_{str(image_number)}", image_url, "images/")


if __name__ == "__main__":
    main()
