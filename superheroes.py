import requests

API_KEY = 2619421814940190
URL = 'https://superheroapi.com/api/2619421814940190/'


# Кто самый умный супергерой? Есть API по информации о супергероях. Нужно определить кто самый умный(intelligence)
# из трех супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name
#
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

def hero_int(name):
    response = requests.get(URL+'search/'+name)
    json_data = response.json()
    hero_id = json_data['results'][0]['id']
    intelligence = json_data['results'][0]['powerstats']['intelligence']
    return intelligence

# Ниже - часть кода из исходной домашки

# def most_intell(heroes_list):
#     intell = 0
#     hero_name = ''
#     for superhero in heroes_list:
#         if int(hero_int(superhero)) > int(intell):
#             intell = hero_int(superhero)
#             hero_name = superhero
#     # return print(f'Most intelligence -- {hero_name} ({intell})')
#     return hero_name

# superheroes = ['Hulk', 'Captain America', 'Thanos']
# print(most_intell(superheroes))

