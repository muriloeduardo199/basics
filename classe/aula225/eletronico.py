from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado  = False

    
    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if  self._ligado:
            self._ligado = False




class SmartPhone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()





    def desligado(self):
        super().ligar()