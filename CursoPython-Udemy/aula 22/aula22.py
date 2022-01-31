"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# texto = 'valor'
# lista = [1, 2, 3, 4, 'jose', True, 10.5]
######################################################
"""
#  (+)    0      1       2    3    4
lista = ['A', 'Bacana', 'C', 'D', 'E']
#  (-)    5      4       3    2    1
#         01234
string = 'ABCDE'

print(lista[1])
print(lista[1][2])
print(lista[-2])
print(string[1])

lista[4] = 'MUDEI O ELEMENTO DA LISTA!'
print(lista)
"""

# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1+l2

# l1.extend(l2) # l1 adicionou os elementos de l2 na lista.

# l2.append('b')
# print(l2)
# print(l2[3])

# print(l1)
# print(l2)
# print(l3)
#####################################
# l1 = [1,2,3]
# l2 = [4,5,6]
#
# l2.insert(0, 'banana')
# print(l1)
# print(l2)
##############################################
#
# l2 = [4,5,6]
# print(l2)
# l2.insert(0, 'banana')
# print(l2)
# l2.pop()
# print(l2)
##############################################
#     0 1 2 3 4 5 6 7 8
# l1 = [1,2,3,4,5,6,7,8,9]
# l1.insert(0, 'banana')
# print(l1)
# del(l1[3:6])
# print(l1)
# l2 = ['2', 'foca', 4, 9.8]
# l1.extend(l2)
# print(l1)
# l1.append(l2)
# print(l1)
#######################################
# l1 = [1,2,3,4,5,6,7,8,9]
# print(max(l1))
# print(min(l1))
###################################
# l2 = list(range(0, 100, 8))
# print(l2)
#################################

# l2 = list(range(0, 100, 8))

# l2 = [0,1,2,3,4,5,6,7,8,9]
#
# soma = 0
# for valor in l2:
#     soma += valor
#
# print(soma)
############################################
#
# l1 = ['string', True, 10, -20.5]
#
# for elem in l1:
#     print(f'O tipo de cada elemento em l1 é {type(elem)} e seu valor é {elem}. ')

###############################################

secreto = 'perfume'
digitados = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu.')
        break

    letra = input('Digite um letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale! digite apenas uma letra.')
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f'UhU!! A letra "{letra}" existe na palavra secreta.')

    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Legal! você ganhou!!!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}.')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
