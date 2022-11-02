"""OPerador ternario em python"""

# logged_user = True
# msg= 'ususario logado' if logged_user else 'usuario precisa logar'

# print(msg)

idade = input('qual a sua idade?')
if not idade.isnumeric():
    print('voce precisa digitar apenas numeros')

else:
    idade= int(idade)
    e_de_maior = (idade >=18)
    msg= 'pode acessar' if e_de_maior else 'nao pode acessar'
    print(msg)