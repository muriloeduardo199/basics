class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome= nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...






c1 = Cliente('Murilo', 'Otavio')
c1.falar_nome()
a1= Aluno('BEATRIZ', 'FERREIRA')
a1.falar_nome()

help(Aluno)