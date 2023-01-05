violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код

li = []
ok = True
k = int(input('Сколько песен выбрать? '))
for i in range(1, k + 1):
    s = input('\nВведите название ' + str(i) + ' песни: ')
    ok = True
    for j in violator_songs:
        a = []
        a.extend(j)
        for l in a:
            if s == l:
                li += [s]
                ok = False
    if ok:
        print('\nОшибка. Такой песни в плейлисте нет!')
        break
    if i == k:
        su = 0
        for i in violator_songs:
            if i[0] in li:
                su += i[1]
        print('\nОбщее время звучания песен:', float(round(su, 2)))

    