# TODO здесь писать код

dataset = {}

country_num =  int(input('Кол-во стран: ', ))

for i in range(0, country_num):
    value = input(' {} страна: '.format( i + 1)).split()
    for town in value [1:]:
        dataset[town] = value[0]

for i in range(1, 4):
    city = input('Город: '.format(i))

    country = dataset.get(city)

    if country:
        print('Город {} расположен в стране{}.'.format(city,country))

    else:
        print('По городу {} данных нет.'.format(city))