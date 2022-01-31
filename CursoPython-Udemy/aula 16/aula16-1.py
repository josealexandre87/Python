"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
from time import sleep

while True:
    try:
        num = int(input('Digite um número inteiro: '))

        if num % 2 == 0:
            print(f'O número {num} é PAR!')
        else:
            print(f'O número {num} é IMPAR!')
        break
    except:
        print('Digite um número válido')
        sleep(1)