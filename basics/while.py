contador = 0


# while contador <=100:

#     contador += 1
#     if contador ==6:
#         print('nao vou mostrar o 6')
#         continue
#     if contador >= 10 and contador <= 27:
#         print('nao vou mostrar', contador)
#         continue

#     print(contador)

#     if contador == 40 :
#         break

# qtd_linhas=5
# qtd_colunas=5
# linha=1 
# qtd_z=5
# while linha <= qtd_linhas:
#     coluna=1
#     while coluna <= qtd_colunas:
#         coluna+=1
#         z=1
#         while z <= qtd_z:
#             print(f'{linha=} {coluna=} {z=}')
#             z+=1
#     linha+=1

contador = 0
nome = 'murilo eduardo'
nova_string = ''
tamanho_nome = len(nome)
while contador < tamanho_nome:
    letra = nome[contador]
    nova_string += f'*{letra}'
    contador+=1
nova_string += '*'
print(nova_string)