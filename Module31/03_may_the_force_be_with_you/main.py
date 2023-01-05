# TODO здесь писать код
import requests
import json

url = 'https://swapi.dev/api/people/'

response = requests.get(url)

res = response.json()

home_world = requests.get(res['results'][0]['homeworld'])

res_home_world = home_world.json()

count = res["count"]

for i in range(0, 10):
    print('=' * 70)
    print('Имя:',res['results'][i]['name'])
    print('Рост:',res['results'][i]['height'])
    print('Вес:',res['results'][i]['mass'])
    print('Родная планета:',res_home_world["name"])
    print('Ссылка на информацию о родной планете.',res['results'][i]['homeworld'])