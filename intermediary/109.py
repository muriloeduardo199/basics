# combinations, permutaions e product - itertools
# combinacao- ordem nao importa - iteravel + tamanho do grupo
# permutacao - ordem Importa 

# produto - ordem importa e repete valores unicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep= '\n')


pessoas = [
    'joao', 'joana', 'luiz', 'leticia'
]

camisetas = [
    ['preta', 'azul'],
    ['p','m'],
    ['masculino', 'feminino']
]

print_iter(product(*camisetas))