import os


caminho = os.path.join('/home', 'murilo', 'basics')




for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho,pasta)
    print(caminho_completo)
    continue
    if not os.path.isdir(caminho_completo):
        continue

    for arquivo in os.listdir(caminho_completo):
        print(arquivo)