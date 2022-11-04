def funcao(msg, nome):
    nome=nome.replace('e','3')
    msg= msg.replace('e','4')
    print(msg,nome)


# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))



# def func(*args):
#     args= list(args)
#     args[0] = 20
#     print(args)


def func(*args, **kwargs):
    print(args)
    print(kwargs)

    nome= kwargs.get('nome')
    print(nome)

lista= [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='murilo', sobrenome='eduardo')