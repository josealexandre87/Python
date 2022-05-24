
from itertools import groupby, tee #(tee faz uma cópa do iterador)

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Joaquim', 'nota': 'A'},
    {'nome': 'Augusto', 'nota': 'B'},
    {'nome': 'Fernando', 'nota': 'B'},
    {'nome': 'Miguel', 'nota': 'B'},
    {'nome': 'Rafael', 'nota': 'B'},
    {'nome': 'Carlos', 'nota': 'B'},
    {'nome': 'Tobias', 'nota': 'B'},
]

ordena = lambda item: item['nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
    print()