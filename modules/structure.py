import requests
from bs4 import BeautifulSoup


headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}


def get_structure(link=None, tags=None):
    """
    Получение структуры для сайта.
    Без указания URL, запрашивается структура для freestylo.ru
    """
    try:
        url = "https://freestylo.ru/"

        if link is not None:
            url = link

        req = requests.get(url, headers)
        soup = BeautifulSoup(req.content, 'html.parser')  # TODO: Для получения вложенной структуры переделать поиск.

        if tags is None:
            tags = [tag.name for tag in soup.find_all()]  # TODO: Сразу выполнять подсчёт.
        else:
            tags = tags.split(",")  # Из строки запроса переделываем в список.

        tag_counter = {}

        for tag in set(tags):  # Создаём словарь для подсчёта тэгов.
            tag_counter[tag] = 0

        for tag in tags:  # Подсчитываем тэги.
            tag_counter[tag] += 1

        return tag_counter
    except requests.exceptions.ConnectionError:
        return {"status": "Connection error!"}
