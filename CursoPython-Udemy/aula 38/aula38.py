"""
1 - Crie uma função1 que reebe uma função2 como parâmetro e
retorne o valor da função2 executada.

"""
def ola_mundo():
    return 'Olá Mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo) # a função mestre está chamando a função ola_mundo
print(executando)

var = ola_mundo() # atribuiu o valor de retorno da função ola_mundo() à variavel var
print(var)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e
retorne o valor da função2 executada.  Faça a função1 executar
duas funções que recebem um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'JOSE')
executando2 = mestre(saudacao, 'JOSE', saudacao='Bom dia!!')
print(executando)
print(executando2)