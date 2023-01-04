import json



CAMINHO_JSON = 'aula127.json'

class Pessoa :
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    

p1= Pessoa('joao', 33)
p2= Pessoa('joana', 23)
p3= Pessoa('maria', 13)
bd= [vars(p1), p2.__dict__, vars(p3)]



def fazer_dump():
    with open(CAMINHO_JSON, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('ele e o main')
    fazer_dump()