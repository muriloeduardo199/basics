import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME,  'basics')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'classe')
NOVA_PASTA = os.path.join(DESKTOP,  'NOVA_PASTA')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dir, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dir:
        caminnho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        print(caminnho_novo_diretorio)
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)