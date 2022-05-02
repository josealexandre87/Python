"""
Zip - Unindo iteráveis ##### UNE ATÉ A MENOR LISTA!
Zip_longest - ESTÁ NO MODULO -> Itertools   (Tem que IMPORTAR!!!!)
"""

from itertools import zip_longest, count  # IMPORTADO Zip_Longest # IMPORTADO count
#count() é um GERADOR! ter cuidado com os loops infinitos, trava a maáquina.
indice = count() ####!!!!! NÃO USAR count() COM Zip_longest, VAI TRAVAR A MÁQUINA!!!!!!!!!
# Lista 1
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
# Lista 2
estados = ['SP', 'MG', 'BA'] # ZIP VAI UNIR APENAS 3 estados!!!

################## ZIP ##############################
cidades_estados = zip(
    indice,
    estados,
    cidades
)
# DESEMPACOTAMENTO DOS DADOS
for indice, estados, cidades in cidades_estados:
    print(indice, estados, cidades)
# print(list(cidades_estados)) # CONVERTIDO EM UMA LISTA!

# SAIDA:
# ('São Paulo', 'SP')
# ('Belo Horizonte', 'MG')
# ('Salvador', 'BA')

# - MONTE BELO ficou fora!

################### ZIP_LONGEST ###########################

# UNE A PARTIR DA MAIOR LISTA E PREENCHE COM 'NONE' O QUE NÃO ENCONTRAR.
#cidades_estados = zip_longest(estados, cidades, fillvalue='Estado') # o PARÂMETRO fillvalue atribue um nome ao
#valor NONE de zip e zip_longest. Ou seja, irá aparecer o que foi atribuido em fillvalue, no caso 'Estado'.
#print(list(cidades_estados)) # CONVERTIDO EM UMA LISTA
# SAÍDA:
# ('São Paulo', 'SP')
# ('Belo Horizonte', 'MG')
# ('Salvador', 'BA')
# ('Monte Belo', None)


# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))