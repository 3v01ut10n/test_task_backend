import requests
from bs4 import BeautifulSoup

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}


def get_structure_default():
    """Получение структуры для сайта freestylo.ru"""
    url = "https://freestylo.ru/"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    tags = [tag.name for tag in soup.find_all()]  # TODO: Оптимизация с созданием счётчика и записью сразу в него.
    tag_counter = {}

    for tag in set(tags):  # Создаём словарь для подсчёта тэгов.
        tag_counter[tag] = 0

    for tag in tags:  # Подсчитываем тэги.
        tag_counter[tag] += 1

    return tag_counter
