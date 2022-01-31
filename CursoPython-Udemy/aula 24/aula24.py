"""
Split, Join, Enumerate em Python
* Split - Divide uma string #str
* Join - Junta uma lista # str
* Enumerate - Enumera elementos da lista #lista # objetos iteráveis

"""
"""
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista1 = string.split(' ')
lista2 = string.split(',') # split() separa em uma lista a string definida.

for a in lista1:
    print(f'A palavra {a} apareceu {lista1.count(a)}x na frase.') #coutn() conta quantas vezes o elemento apareceu.
"""
#########################################################
"""
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista1 = string.split(' ')
lista2 = string.split(',') # split() separa em uma lista a string definida.

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi: {palavra} ({contagem}x)')
"""
#################################################################
# string = 'O Brasil é o o o país do futebol, o Brasil é penta'
# lista1 = string.split(' ')
# lista2 = string.split(',') # split() separa em uma lista a string definida.
#
# for valor in lista2:
#     print(valor.strip().capitalize())
#####################################################

# string = 'O Brasil é penta.'
# lista = string.split(' ')
# string2 = ','.join(lista)
#
# print(string)
# print(lista)
# print(string2)

#######################################
#ENUMERATE
# string = 'O Brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

##############################

# Lista em lista
# lista = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
#
# for v in lista:
#     print(v)
########################################
lista = [
    [0,'JOSE'],
    [1,'FELIPE'],
    [2,'MARIA']
]

for indice, nome in lista: # mesma saída que enumerate!!!
    print(indice, nome)

lista = ['JOSE', 'FELIPE', 'MARIA']

for indice, nome in enumerate(lista): # ENUMERATE!! percorre os elementos da lista e dá o indice e o elemento.
    print(indice, nome)

# n1, n2, n3 = lista      #DESEMPACOTAMENTO
#
# print(n2)