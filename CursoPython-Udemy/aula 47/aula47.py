"""

Dictionary/Set Comprehension em Python

"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]
# USAR CHAVES {} para ser dicionário
# d1 = {x:y*2 for x, y in lista} # multiplica os valores do dicionário
# d1 = {x.upper():y.upper() for x, y in lista} # consegue colocar metodos nas variáveis do DICT
# d1 = {x:y for x, y in enumerate(range(5))} # cada k e v do DICT fica com números de 0 a 4

# SEM CHAVE E VALOR, AS {} FAZEM A VARIÁVEL VIRAR UM SET ( CONJUNTO )
# d1 = {x for x in range(5)} SET
d1 = {f'chave_{x}': x**2 for x in range(5)} #DICT com nome do índice do range(5) e value elevado ao quadrado.

print(d1, type(d1))
