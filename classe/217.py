class Cliente:
    def __init__(self, nome):
        self.nome =  nome 
        self.enderecos =[]

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua,numero))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('apagando,', self.rua, self.numero)



cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 4571)
cliente1.lista_enderecos()




print('aqui termina meu codigo')