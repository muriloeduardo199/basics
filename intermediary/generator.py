import sys

iterable = ['EU', 'tenho', '__iter__']

iterator = iter(iterable)

lista = [n for n in range(10000)]


generator = (n for n in range(10000))

print(sys.getsizeof(lista))

print(sys.getsizeof(generator))


for n in generator:
    print(n)