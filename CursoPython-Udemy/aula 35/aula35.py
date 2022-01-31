"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""

"""
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

"""

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o
valor do primeiro número somado do segundo do percentual do mesmo.
"""

"""
4 -  Fizz Buzz - Se o parâmetro da função fo divisível por 2, return fizz. Se o parâmetro da função for divisível por 5,
retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número
enviado.
"""
######### exercício 1 #############

def saudacao(saud='Olá!', name='Criatura!') -> str:
    return f'{saud}! Como você está, {name}?'


n1 = saudacao('Tudo bem?', 'JOSÉ')
n2 = saudacao()
print(n1)
print(n2)

######### exercício 2 #############

def soma_3(n1, n2, n3):
    return n1+n2+n3


soma = soma_3(1, 3, 5)

print(f'O resultado foi {soma}!!')

######### exercício 3 #############

def porcentagem(valor, percentual):
    n_1 = valor
    n_2 = (valor*percentual/100)
    n_3 = n_1 + n_2
    return print(f' {n_1} + {n_2} é igual a {n_3}.')


porcentagem(10, 50)
porcentagem(500, 20)
porcentagem(100, 5)
porcentagem(456, 125)

######### exercício 4 #############

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FIZZBUZZ'
    elif n % 5 == 0:
        return 'BUZZ'
    elif n % 3 == 0:
        return 'FIZZ'
    else:
        return n

print(fb(3))
print(fb(5))
print(fb(45))