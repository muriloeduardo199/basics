class Animal:
    nome = 'leao'

    def __init__(self, nome):
        self.nome= nome
    

    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)




leao = Animal(nome='leao')

print(leao.executar('maçã'))