"""
Funções (def) em Python - return - Aula 16 (parte 2)
"""
def divisao(n1, n2):
    if n2 == 0:
        return
    return n1/n2


divide = divisao(8, 3)

if divide:
    print(f'{divide:.2f}') # se não houvesse um eslse, o resultado seria "NONE".
else:
    print('Conta inválida! Defina um número para n2 diferente de zero(0)')


######################

def dumb():
    return ('Luiz', 'Otávio')

var = dumb() # uma variável pode receber uma função e torna-se um objeto do tipo'Function'.

print(var[1], type(var), id(dumb()), id(var)) #pelo id nota-se que os dois tem o mesmo endereço na memória.
# (saída do print>>>>) Otávio <class 'tuple'> 2324159792064 2324159792064