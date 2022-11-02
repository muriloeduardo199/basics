variavel = ['luiz otavio', 'Joaozinho', 'maria']

# for valor in variavel:
#     if valor.startswith('J'):
#         print('Comeca com J', valor)
#     else:
#         print('nao comeca com J', valor)



for valor in variavel:
    if valor.lower().startswith('j'):
        break


else:
    print('nao existe uma palavra que comeca com J')