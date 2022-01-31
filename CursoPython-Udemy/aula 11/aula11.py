"""
Operadores Relacionais:

==    -  igualdade
>     - maior que
<     - menor que
>=    - maior que ou igual a
<=    - menor que ou igual a
!=    - diferente

"""

variavel = 'valor'

num_1 = 2 #int
num_2 = 2 #int

#print(num_1, num_2)
#print(num_1 == num_2)

expressao = (num_1 >= num_2)

print(expressao)

#print(2 == 2)
#print(2 == 1)
nome = input('Qual é o seu nome?: ')
idade = input('Quntos anos você tem? ')

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')

