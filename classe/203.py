class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.idade= idade
        self.nome = nome

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade




p1 = Pessoa('Joao', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())