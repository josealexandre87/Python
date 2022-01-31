"""
while em Python
utilizado para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""

#while condicao:
   # pass
"""
while True: # loop infinito
    nome = input('Qual é o seu nome: ')
    print(f'Olá {nome}!')

print('Essa expressão não será executada!')
"""
'''
x = 0
while x<100:
    print(x)
    x += 1 #ou x = x+1
print('Acabou!')
'''
'''
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue

    print(x)
    x += 1 #ou x = x+1
print('Acabou!')
'''
"""
x = 0
while x < 10:
    if x == 3:
        x += 1
        break

    print(x)
    x += 1 #ou x = x+1
print('Acabou!')
"""
"""
x = 0 #coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x += 1

print('Acabou!')
"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um Operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número inteiro')
        continue

    num_1 = int(num_1)
    num_2  = int(num_2)


    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido.')

    sair = input('Deseja continuar calculando? [s]im ou [n]ão: ').strip().lower()
    if sair == 'n':
        print('Até mais!')
        break