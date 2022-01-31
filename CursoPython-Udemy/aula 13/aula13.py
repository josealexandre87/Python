"""
len  - funciona com strings ( não funciona com tipos numéricos.)
# o len conta também os espaços em branco nas strings.
"""


'''
usuario = input('Digite o usuário: ')
qtd_caracteres = len(usuario) # o len já gera um resultado do tipo int (inteiro).

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')

print(usuario, qtd_caracteres, type(qtd_caracteres))
'''

string1 = input('Digite uma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade de caracteres totais digitados foi: {len(string1) + len(string2)}')
