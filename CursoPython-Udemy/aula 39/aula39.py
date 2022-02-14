"""
Expressões Lambda (funções anônimas) em Python
"""

# def func(arg, arg2):
#     return arg * arg2
#
# var = func(2,2)
# print(var)
#
# a = lambda x, y: x * y
# print(a(2,2))

# def func(item):
#     return item[1]

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

# lista.sort(key=func, reverse=True)
# print(lista)

print(sorted(lista, key=lambda i: i[0], reverse=True)) #função anônima lambda. os parâmetros e return já estão nela.