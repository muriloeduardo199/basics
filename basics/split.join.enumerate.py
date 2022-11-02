"""split, join, enumerate
split = dividir uma string 
join = junta uma string
enumerate = enumera elementos da lista
"""

# string= "Murilo o o o o o Eduardo dos Santos Lima"
# lista_1= string.split(' ')
# lista_2 = string.split(',')

# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes= lista_1.count(valor)

#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra= valor


# print(f'A palavra que apareceu mais vezes e {palavra} ({contagem}x)')

string = 'o brasil e penta'
lista = string.split(' ')
string2= ','.join(lista)


for indice, valor in enumerate(lista):
    print(indice, valor)

