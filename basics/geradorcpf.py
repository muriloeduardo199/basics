"""validacao de cpf"""
from random import randint

numero = str(randint(100000000, 999999999))

novo_cpf= numero

reverso=10
contador=0
for index in range(19):
    if index >8:
        index-=9

    contador+= int(novo_cpf[index]) * reverso


    reverso -= 1
    if reverso < 2:
        reverso = 11
        d= 11 - (contador % 11)

        if d > 9:
            d=0
        contador = 0
        novo_cpf += str(d)


print(novo_cpf)
