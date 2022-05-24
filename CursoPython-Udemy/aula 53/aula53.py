"""

Count - Intertools (Contadores Infinitos)
"""

from itertools import count

# contador = count(start=-5, step=1)
#
# for valor in contador:
#     print(round(valor, 2))
#     if valor >=10 or valor <= -10:
#         break


contador = count()

lista = ['luiz', 'joão', 'Maria', 'josé', 'silva']
lista = zip(contador, lista)
print(list(lista))


# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))