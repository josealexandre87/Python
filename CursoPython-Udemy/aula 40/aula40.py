"""
TUPLAS
"""

t1 = ()

print(type(t1))


t2 = 1, 2, 3, 4, 5
t3 = 6, 7, 8, 9, 10
t4 = t2 + t3 #concatenar as tuplas

print(t4)
####################################################
n1, n2, n3, *_, n4 = t4 #diz pra concatenação parar ali. e depois de ' *_' o n4 recebe o ultumo calor da tupla t4!!

print(n1, n2, n3, n4)
##################################################
tu1 = (1, 2, 3, 4, 5, 6)
tu1 = list(tu1)
tu1[1] = 3000
tu1 = tuple(tu1)

print(tu1)