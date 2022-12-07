pessoa = {
    'nome': 'aline',
    'sobrenome': 'souza',
}

# a,b = pessoa.keys()
# print(a,b)

def argument( *args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


argument(**pessoa)