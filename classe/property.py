class Caneta:
    def __init__(self, cor):
        self.cor_tinta_escolhar =cor




    @property
    def cor(self):
        return self.cor_tinta_escolhar


    @property
    def cor_tampa(self):
        return 123456

caneta = Caneta('azul')
print(caneta.cor)
print(caneta.cor_tampa)
