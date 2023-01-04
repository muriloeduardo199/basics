import json
from aula207 import CAMINHO_JSON, Pessoa, fazer_dump


fazer_dump()


with open(CAMINHO_JSON, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1= Pessoa(**pessoas[0])
    print(p1.nome)
