def reverse_float(num):
    parts = str(num).split('.')
    reversed_parts = [''.join(reversed(part)) for part in parts]

    return float( '.'.join(reversed_parts) )

a = reverse_float(input('a'))
b = reverse_float(input('b'))

print('rvs a', a)
print('rvs b', b)
print('total', a + b)