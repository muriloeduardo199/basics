from dataclasses import dataclass

@dataclass
class Lampada:

    lampada: bool


    def ligar(self) -> bool:
        self.lampada = True
        
    
    def desliga(self)-> bool:
        self.lampada = False
        

    def condicao(self):
        return self.lampada



lamp_instance = Lampada(True)

print(lamp_instance.desliga())

print(lamp_instance.condicao())

