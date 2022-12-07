

"""
len- quantas chaves
keys- iteravel com chaves
values- iteravel com valores
items-iteravel com chaves e valores
setdefault- adiciona valor se a chave nao existir
copy- retorna uma copia rase (shallow copy)
get- obtem uma chave
pop- apaga um item com a chave especificada
popitem- apaga o ultimo item adicionado
update- atualiza um dicionario com outro
"""
import copy

pessoa = {
    'nome': 'murilo eduardo',
    'sobrenome': 'santos lima',
    'idade ': 29
}

d1= {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2]
}


d2= d1.copy()

d2= copy.deepcopy(d1)
print(d1)
print(d2)
# pessoa.setdefault('cor', 'parda')

# print(pessoa.keys())

# print(pessoa.values())

# print(pessoa.items())