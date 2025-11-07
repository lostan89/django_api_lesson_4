import requests
from environs import Env
from additional import save_image_to_path


def get_nasa_image(api_key, count):
    api_url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": api_key, "count": count}
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    nasa_photo = response.json()
    image_url = []
    for image in nasa_photo:
        url = image.get("url")
        if url:
            image_url.append(url)
    return image_url


def main():
    env = Env()
    env.read_env()
    api_key = env.str("NASA_API_KEY")
    nasa_image = get_nasa_image(api_key, 30)
    for image_number, image_url in enumerate(nasa_image):
        save_image_to_path(f"nasa_apod_{str(image_number)}", image_url, "images/")


if __name__ == "__main__":
    main()
