"""
ENUMERATE - Enumerarelementos da lista #list
"""

lista = [
    #0  1  2 de cada Elemento das listas dentro da variável lista.
    [1, 2, 3],  #indice 0 da variavel 'lista'
    [4, 5, 6],  #indice 1 da variavel 'lista'
    [7, 8, 9]   #indice 2 da variavel 'lista'
]
enumeradas = list(enumerate(lista))
print(enumeradas[1][1])  #[4, 5, 6]
print(enumeradas[0][1])
print(enumeradas[2][1])
print(enumeradas[2][0])
print(enumeradas[1][0])
"""
[   #0      #1
    (0, [1, 2, 3]), #indice 0 da variavel 'lista' 
    (1, [4, 5, 6]), #indice 1 da variavel 'lista'
    (2, [7, 8, 9])  #indice 2 da variavel 'lista'
]
"""
for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)