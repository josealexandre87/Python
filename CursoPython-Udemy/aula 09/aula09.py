"""
Entrada de dados
"""
"""
nome = input("Qual o seu nome? ") # sempre retorna uma string
idade = input('Qual é a sua idade? ')

ano_nascimento = 2019-int(idade) # TEM que ser feito o type casting, pois a função input() só retorna string!!!

print() # separa um espaço
print(f'O usuário digitou {nome} e o tipo da variavél é {type(nome)} e {nome} tem '
      f'{idade} anos de idade e nasceu em {ano_nascimento}.')
"""

numero_1 = int(input('Digite um número: ')) #Foi inserito o Type Cast 'int' para transformar o input() str em "int".
numero_2 = int(input('Digite outro número: '))#Foi inserito o Type Cast 'int' para transformar o input() str
# em "int".

print(numero_1 + numero_2) # caso não fosse usado o Type Cast a função print() não poderia somar os dois inteiros,
# mas ela iria concatenar os números digitado e com saída na forma de string.



