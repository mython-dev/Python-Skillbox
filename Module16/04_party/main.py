guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:
    print('Сейчас на вечернике', len(guests), 'человек', guests)

    guests = input('Гость пришел или ушел?: ')

    if guests=='пришел':
        if len(guests) < 6:
            guests.append(name)
            print('Привет', name)

        else:
            print('Прости ', name, ', но мест нет', sep="")
    elif guests == 'ушел':
        print('Пока', name)
        guests.remove(name)