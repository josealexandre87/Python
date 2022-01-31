"""
Desempacotamento de listas no Python

"""

lista = ['José', 'João', 'Maria', 2, 3, 4, 5, 6]

## O '*' serve para delimitar os ítens vc quer para as variaveis antes ou depois da lista formada pelo '*'.

# n1, n2, n3, *outra_lista = lista # '*' gera uma lista com os números restantes da lisa().
# print(f' {n1}, {n2} e {n3}.')
*_, n1, n2, n3 = lista # '*' gera uma lista com os números das variáveis finais da lisa().
#!!!USAR O '*_' indica para outros Devs que vc não utilizará os valores restantes da lista().
print(n1, n2, n3)
