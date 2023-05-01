# Задача №2
# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон. Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.

# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443

# Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!

import requests

TOKEN = 'token'
FILE_PATH = 'data.txt'

def upload_to_yandex_disk(file_path):
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {'Authorization': f'OAuth {TOKEN}'}

    params = {"path": f"/{file_path.split('/')[-1]}", "overwrite": "true"}
    response = requests.get(url, headers=headers, params=params)

    href = response.json().get('href')

    with open(file_path, 'rb') as f:
        requests.put(href, files={'file': f})

    print(f"Файл {file_path} успешно загружен на Yandex.Disk")

upload_to_yandex_disk(FILE_PATH)