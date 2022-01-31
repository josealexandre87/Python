#        índices
#        0123456789......................33

# frase = 'o rato roeu a roupa do rei de roma'   # Iterável
# tamanho_frase = len(frase)  #34 ( começando do zero(0) )
# contador = 0
# nova_string = ''
#
# while contador < tamanho_frase:
#     # print(frase[contador], contador)
#     #nova_string += frase[contador]
#     letra = frase[contador]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contador += 1                 #ctrl + / ---- COMENTA TUDO!
#     print(nova_string)
# print(f'{nova_string:#^50}!!!!')


frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)  #34 ( começando do zero(0) )
contador = 0
nova_string = ''

input_usuario = input('Qual letra deseja colocar maiúscula?: ')

while contador < tamanho_frase:
    # print(frase[contador], contador)
    #nova_string += frase[contador]
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1                 #ctrl + / ---- COMENTA TUDO!
    print(nova_string)
print(f'{nova_string:#^50}!!!!')