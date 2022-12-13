string = 'Murilo'
metodo = 'upper'


if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('nao existe metodo', metodo)