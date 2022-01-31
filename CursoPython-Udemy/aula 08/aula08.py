"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variável com ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores da tela usando F-Strings *(com as chaves)
"""

nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80
imc = peso/altura**2
ano_atual = 2021
nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
