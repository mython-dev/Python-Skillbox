# TODO здесь писать код


# Задача 2. Шеренга

one_class = []
two_class = []

for i in range(160, 176 + 2, 2):
    one_class.append(i)
print(one_class)

for j in range(162, 180 + 3, 3):
    two_class.append(j)
print(two_class)

one_class.extend(two_class)

print(sorted(one_class))