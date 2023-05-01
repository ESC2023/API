# Задача №1
# Кто самый умный супергерой?
# Есть API по информации о супергероях с информацией по всем супергероям. Нужно определить кто самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos.

# Решение:
# В этой программе мы используем библиотеку requests для получения данных о каждом из супергероев из API. Затем мы анализируем показатель intelligence каждого героя и определяем максимальное значение и соответствующий ему супергерой.

import requests

API_URL = "https://akabab.github.io/superhero-api/api/"
HEROES = ["Hulk", "Captain America", "Thanos"]

max_intelligence = -1
smartest_hero = None

for hero_name in HEROES:
    response = requests.get(API_URL + "id/" + str(HEROES.index(hero_name) + 1) + ".json")
    if response.status_code == requests.codes.ok:
        hero_data = response.json()
        intelligence = int(hero_data["powerstats"]["intelligence"])
        if intelligence > max_intelligence:
            max_intelligence = intelligence
            smartest_hero = hero_name

if smartest_hero is not None:
    print("Самый умный супергерой это", smartest_hero)
else:
    print("Не удалось определить самого умного супергероя")