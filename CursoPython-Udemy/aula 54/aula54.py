"""

Combinations, Permutations and Product - itertools

Combinação - Ordem não importa - Ambos não repetem valores únicos
Permutação - --//--

Produto - Ordem importa e repete valores únicos.
"""

from itertools import combinations, permutations, product

#Ordem não importa e não repete valores únicos
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in permutations(pessoas, 2):
    print(grupo)
print()

#Ordem não importa e não repete valores únicos
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 2):
    print(grupo)
print()

#Ordem importa e repete valores únicos.
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in product(pessoas, repeat=2):
    print(grupo)
print()