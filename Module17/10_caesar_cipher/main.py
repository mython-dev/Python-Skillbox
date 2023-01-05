# TODO здесь писать код


def CaesarCipherChar(c, n):
    alpha = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alpha2 = alpha.upper()
    if c.isupper():
        return(alpha2[(alpha2.index(c) + n) % len(alpha2)])
    elif c.islower():
        return(alpha[(alpha.index(c) + n) % len(alpha)])
    else:
        return(c)
 
s = input('Введите сообщение: ').strip()
n = int(input('Введите сдвиг: '))
res = 'Зашифрованное сообщение: '
for c in s:
    res += CaesarCipherChar(c, n)
print('Result: "' + res + '"')
