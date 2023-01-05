# TODO здесь писать код

number = int(input('Введите длину списка: '))
numbers_list = []
count = -1
for x in range(0, number):
    count += 1
if count % 2 == 0:
    numbers_list.append(1)
else:
    x = x % 5
numbers_list.append(x)
print(numbers_list)