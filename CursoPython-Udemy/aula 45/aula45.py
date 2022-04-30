"""
LIST COMPREHENSION EM PYTHON
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = [variavel * 2 for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['luiz', 'Mauro', 'Maria']
ex4 = [nome.replace('a', '@') for nome in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex5 = [(x,y) for x, y in tupla]
ex6 = [(y,x) for x, y in tupla] #inverteu o valor de x e y da tupla
ex5 = dict(ex5) # transforma a lista ( que era tupla) em dicionário!!!
ex7 = dict(tupla) # transforma a tupla em dicionário!!!

l3 = list(range(100))
ex8 = [item for item in l3 if item % 2 == 0] #lista de PARES
ex9 = [item for item in l3 if item % 3 ==0 if item % 8 == 0] # ex9 será uma lista de 0 a 99 de item divisíveis por 3 e por 8!
ex10 = [item if item % 3 == 0 else 'N' for item in l3] #inclui o ELSE na list Compr...
ex11 = [item if item % 3 == 0 and item % 8 == 0 else 'N' for item in l3] #inclui o AND na List Compr...

print(ex2)
print(ex3)
print(ex4)

print(ex5)
print(ex6)
print(ex7)
print(ex5['chave']) # imprime na tela apenas o VALUE da KEY = 'chave'... no DICT ex5.
print(ex8)
print(ex9)
print(ex10)
print(ex11)