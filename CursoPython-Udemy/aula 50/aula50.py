"""
Exercícios Propostos - Somar valores de uma LISTA usando o metodo List Comprehension.

"""

carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

# print(carrinho)
# print(carrinho[1][1])

# for produto in carrinho:
#     print(produto[1])
##################     SOLUÇÃO 1 sem LIST COMPREHENSION ##############
# total = 0
# for produto in carrinho:
#     total += produto[1]
# print(total)
##################     SOLUÇÃO 2 sem LIST COMPREHENSION ##############
# total = []
# for produto in carrinho:
#     total.append(produto[1])
#
# print(sum(total))


##################  !!!!!!  SOLUÇÃO 3 COM LIST COMPREHENSION !!!!! ##############

total = sum([float(y) for x, y in carrinho]) # em conchetes, será criada uma lista copm valores com ponto flutuante
# do y das tuplas dos produtos. e após, envelopando com a função sum() serão somadas os valores da lista total criada.
print(total)