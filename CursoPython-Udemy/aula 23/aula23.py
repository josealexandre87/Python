"""
For / Else em Python
"""

# variavel = ['Jose Alexandre', 'Joãozinho', 'Maria']

# for valor in variavel:
    # print(valor)
    # break
    # continue
    # print(valor)
    # if valor.startswith('J'):
    #     print('Começa um J')
    # else:
    #     print('Não começa com J')

variavel = ['Jose Alexandre', 'Joãozinho', 'Maria']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'): # startswith('') procura na lista/tupla se tem uma String q começa com a letra definida.
        break
else:
    print('Não exist uma palavra que começa com J')