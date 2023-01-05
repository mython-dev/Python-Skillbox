
# 15.6 Практическая работа (автотесты)

# Задача 1. Генерация списка

number_list = []
number = int(input('Введите целое число: '))

for i in range(1, number):
    if i % 2 != 0:
        number_list.append(i)

print(number_list)

# Задача 2. Турнир

l = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
for i in range(1,len(l),2):
    print(l[i])

# Задача 3. Клетки

cell_list = [3, 0, 6, 2, 10]
cell_range = []
print('Кол-во клеток: ', len(cell_list) - 1)

for i in range (len(cell_list)):
    print('Эффективность', i + 1, 'клетки', cell_list[i])
    if i > cell_list[i]:
        cell_range.append(cell_list[i])
print('Неподходящие значения:', cell_range)

# Задача 4. Видеокарты

nvidia_list = []
new_nvidia_list = []
new_new = []

qty = int(input('Кол-во видеокарт: '))
print()
count = 1
for _ in range(qty):
    card = int(input(str(count) + ' Видеокарта: '))
count += 1
nvidia_list.append(card)
print('Старый список видеокарт: ', *nvidia_list)


# Задача 5. Кино

films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
'Леон', 'Богемская рапсодия', 'Город грехов',
'Мементо', 'Отступники', 'Деревня']
favourites_films = []
films_number = int(input('Сколько фильмов хотите добавить? '))

for i in range(1, films_number + 1):
    print(i, 'фильм: ', end='')
movie = input()
while movie not in films:
    print('Нет такого фильма!')
    movie = input('Выберете другой фильм: ')
else:
    favourites_films.append(movie)

    print('\nСписок любимых фильмов: ')
print(favourites_films)

# Задача 6. Анализ слова

word = input('Введите слово: ')
letters = list(word)
total = 0
for i in letters:
    same_letters = 0
for j in letters:
    if j == i:
        same_letters += 1
    if same_letters > 2:
        continue
    elif same_letters == 2:
        total += 1
        break

# Задача 7. Контейнеры

i, l, k = 0, [int(input('Введите вес контейнера: ')) for _ in range(int(input('Кол-во контейнеров: ')))], \
    int(input('Введите вес нового контейнера: '))

while i < len (l) and l[i] >= k: i += 1

print('Номер, куда встанет новый контейнер: ', i + 1)

# Задача 8. Бегущие цифры

step = 1

l  = [1, 2, 3, 4, 5]

while step <=  5:
    n = l [-step]+ l[: - step]
    print(n)

# Задача 9. Анализ слова 2

s=input()
print('Слово является палиндромом' if s == s[::-1] else 'Слово не является палиндромом')



# Задача 10. Сортировка

# не знаю как решить задачу
