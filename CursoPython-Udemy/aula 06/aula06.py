"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
data_1 = True
data_atual = 2019
peso = 80
imc = peso/altura**2

print('nome:', nome, type(nome)) # nome: Luiz <class 'str'>
print('idade:', idade, type(idade)) # idade: 32 <class 'int'>
print('altura:', altura, type(altura)) # altura: 1.8 <class 'float'>
print('É_maior:', e_maior, type(e_maior)) # É_maior: True <class 'bool'>

print(idade*altura, type(idade*altura)) # 57.6 <class 'float'>

print(nome, 'tem', idade, 'de idade e seu imc é:', imc) # Luiz tem 32 de idade e seu imc é: 24.691358024691358