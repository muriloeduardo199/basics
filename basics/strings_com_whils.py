frase = ' o rato roeu a roupa do rei de roma'

tamanho_frase = len(frase)
nova_string= ''

input_do_usuario= input('qual letra voce quer colocar:')

contador=0
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string+= input_do_usuario.upper()
    else:
        nova_string +=letra
    contador +=1

print(nova_string)        