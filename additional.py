import os
import requests
from urllib.parse import urlparse


def save_image_to_path(image_name, url, path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    filename = image_name + get_ext(url)
    response = requests.get(url)
    response.raise_for_status()

    with open(path + filename, "wb") as file:
        file.write(response.content)


def get_ext(url):
    url_parse = urlparse(url)
    url_path = url_parse.path
    ext = os.path.splitext(url_path)[1]
    return ext
