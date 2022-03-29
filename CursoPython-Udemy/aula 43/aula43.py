"""

CONJUNTOS

add (adiciona), upadate (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
diference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não  em ambos)

"""

# s1 = {1, 2, 3, 4, 5, 6, 7} # elementos imutáveis
#
# for v in s1:
#     print(v)

# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add((82, 83, 84))
# s1.discard(2)
# print(s1)
#
# s2 = set()
# s2.update('Python') # não aparecem em ordem
#
# print(s2)
#
#
# l1 = [1,1,1,2,3,3,3,4,4,5,6,6,6,6,6, 'luiz', 'luiz']
# print(l1)
# l1 = set(l1) # conjuntos removem os elementos DUPLICADOS! importante!
# print(l1)
# l1 = list(l1) # retorna o conjunto em lista, mas em qualquer ordem definida pelo set().....eles não respeitao sequencia.
# print(l1)
# print(l1[-1]) # só acessou o elemento [-1] pois o conjunto foi transformado em lista.

######### TRABALHANDO COM CONJUNTOS ###################
s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}

s3 = s1 | s2 # '|' sinal de UNIÃO - une os conjuntos
s4 = s1 & s2   # '&' sinal de INTERSEÇÃO - pega os elementos em comum
s5 = s1 - s2 # '-' A-B é o sinal de DIFERENÇA - pega todos os elementos que não tem no conjunto da esquerda, mas tem no da direita.
s6 = s2 - s1 # '-' B-A é o sinal de DIFERENÇA - pega todos os elementos que não tem no conjunto da esquerda, mas tem no da direita.
s7 = s1 ^ s2 # '^' diferença simétrica - elementos que tem nos dois, mas não em ambos.

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

l1 = ['jose', 'luiz', 'maria']
l2 = ['joao', 'luiz', 'maria']

if set(l1) == set(l2):
    print('l1 é igual a l2')
else:
    print('L1 é diferente de l2')
