
pessoa = {
    'nome': 'murilo eduardo',
    'sobrenome': 'santos lima',
    'idade ': 29
}


dc = {
    chave: valor
    if isinstance(valor, int) else valor.upper()
    for chave, valor
    in pessoa.items()

}

print(dc)