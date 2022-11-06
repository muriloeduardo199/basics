"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""


# def saudacao(saudacao, nome):
#     print(f'{saudacao} {nome}')

# saudacao('ola', 'Murilo')


"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""


# def soma(n1,n2,n3):
#     print(n1+n2+n3)
# soma(1,2,3)
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def recebendo(valor, percent):
    return valor*(valor*percent/100)

ex=recebendo(50,10)
print(ex)
"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def fb(n):
    if n%3==0 and n%5==0:
        return f'fizzbuzz, {n} e divisivel por 3 e 5'
    if n%5==0:
        return f'fizzbuzz, {n} e divisivel  5'
    if n%3==0:
        return f'fizzbuzz, {n} e divisivel  3'
    return n

from random import randint

for i in range(100):
    teste = randint(0,100)
    print(fb(teste))

# def fb(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return f'fizzbuzz, {n} é divisível por 3 e 5'
#     if n % 5 == 0:
#         return f'buzz, {n} é divisível por 5'
#     if n % 3 == 0:
#         return f'fizz, {n} é divisível por 3'
#     return n


# from random import randint

# for i in range(100):
#     aleatorio = randint(0, 100)
#     print(fb(aleatorio))
