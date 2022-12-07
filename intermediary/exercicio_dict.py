perguntas= [

    {
        'pergunta': 'Quanto e 2+2?',
        'opcoes': ['1', '2','3', '4', '5'],
        'resposta': '4'
    },

    {
        'pergunta': 'Quanto e 5*5?',
        'opcoes': ['25', '55','10', '51', '5'],
        'resposta': '25'
    },

    {
        'pergunta': 'Quanto e 10/2?',
        'opcoes': ['4', '5','2', '1'],
        'resposta': '5'
    },

]


for pergunta in perguntas:
    print('pergunta', pergunta['pergunta'])
    print()

    for i, opcao in enumerate(pergunta['opcoes']):
        print(f'{i})', opcao)
    print()

    escolha = input('escolha uma opcao:')

    if escolha.isdigit():
        ...