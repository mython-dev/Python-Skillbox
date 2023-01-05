# TODO здесь писать код

n = int(input('Введите число: ')) 
class SquareIterator: 
    def __init__(self, n=0): self.n = n 
    def __iter__(self): self.i = 1; return self 
    def __next__(self): 
        if self.i <= self.n: result = self.i ** 2; self.i += 1; return result 
        else: raise StopIteration 
for x in SquareIterator(n): print(x) 
def square_generator(n): 
    i = 1 
    while i <= n: yield i ** 2; i += 1 
for x in square_generator(n): print(x) 
print([x**2 for x in range(1, n + 1)])
