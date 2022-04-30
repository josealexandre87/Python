"""
Iteráveis, Iteradores e Geradores

"""

#ITERÁVEIS
import sys
import time

l1 = [x for x in range(1000)]
l2 = (x for x in range(1000))

for v in l2:
    print(v)

# lista = [x for x in range(1000)]
# print(type(lista))
# lista = (x for x in range(1000))
# print(type(lista))
# print(sys.getsizeof(lista))

# lista = [0, 1, 2, 3, 4, 5]
#
# print(hasattr(lista, '__iter__')) #hasattr é uma função built-in do python e usa o metodo __iter__
# para saber se é ITERÁVEL e __next__ = ITERADOR

import sys
import time
# lista = list(range(100))
#
# print(sys.getsizeof(lista))
# def gera():
#     for n in range(100):
#         yield n #função geradora que gera um iterável sem esperar por todos os elementos
#         time.sleep(0.1)

# def gera():
#         variavel = 'Valor 1'
#         yield variavel
#         variavel = 'Valor 2'
#         yield variavel
#         variavel = 'Valor 3'
#         yield variavel
#
#
# g = gera()
#
# for v in g:
#     print(v)

# print(g) #<generator object gera at 0x0000020BBE309510> VAI FAZER UM GERADOR

# Avaliação preguiçosa  (Lazy evaluation) :
# Avaliação preguiçosa é uma técnica usada em programação
# para atrasar # a computação até um ponto em que o resultado
# da computação é considerado necessário.

