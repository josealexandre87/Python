"""
Operadores Lógicos

and
or
not
in
not in
"""
'''
a = '' # vazio
b = 0 # zero(0) é considerado um boleano False ( significa que está vazio)

if not a: # not inverte a operação.
    print('Por favor, preencha o valor de b.')

nome = 'JOSE'

if 'o' or 'O' in nome:
    print('Existe a letra "o" no seu nome.')
'''
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Jose'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')

