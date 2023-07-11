class Carro:


    def __init__(self,nome, marca, modelo):
        self.nome= nome
        self.marca= marca
        self.modelo= modelo 

    def acelerar(self):
        print(f'o {self.nome} da marca {self.marca} do modelo {self.modelo} esta acelerando')

carro= Carro('voyage', 'VW', '2010')

print(carro.acelerar())

celta= Carro(nome= 'celta', marca='chevrolet', modelo=2009)
print(celta.nome, celta.modelo, celta.marca)