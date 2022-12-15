class Carro:
    def __init__(self, nome):
        self.nome = nome


    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


fusca = Carro('Fusca')

celta = Carro('Celta')


print(celta.nome)
print(celta.acelerar())
print(fusca.nome)
print(celta.acelerar())