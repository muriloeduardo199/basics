# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.



class Pessoa:
    ano = 2022

    def __init__(self, nome, idade):
        self.idade= idade
        self.nome = nome

    @classmethod
    def metodo_de_classe(cls):
        print('ola')


p1= Pessoa('joao', 34)
print(Pessoa.ano)
Pessoa.metodo_de_classe()