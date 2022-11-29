entrada = input('digite um numero:')

# if entrada.isdigit():
#     entrada_int= int(entrada)
#     par_impar = entrada_int %2== 0
#     print(f'o numero e par')

# else: 
#     print('vc nao digitou um numero inteiro')

try :
    entrada_int= int(entrada)
    par_impar = entrada_int %2== 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto= 'par'

    
    print(f'o numero {entrada_int} é {par_impar_texto}')

except:
    print('voce nao digitou um nuemro inteiro')