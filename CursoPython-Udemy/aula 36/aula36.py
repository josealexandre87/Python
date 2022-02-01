"""
Funções (def) em Python - *args **kwargs (parte 3)

*arguments e **Keyword arguments
"""
"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func(1, 4, 5, 6, 7, nome='Jose', a6='5')
print(var[0], var[1])
"""

#################################################
# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#     print(*args, sep=' ♂|♀')
#
#
# func(1,2,3,4,5)

#################################################
# def func(*args):
#     args = list(args) # transformou a tupla de args em uma lista!
#     args[0] = 20 # assim foi possível alterar o argumento [0] da lista para 20, pois a tupla é imutável.
#     print(args) # printa args com o indice [0] = 20
#
#
# func(1,2,3,4,5)

##################################################
# lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista #*n vai ter uma lista com os elementos restantes de lista() logo apoós o desempacotamento de n1 e n2.
# print(n1, n2, n)

####################################################
# lista = [1,2,3,4,5]
# print(*lista, sep=', ♂') #somente o '*' desempacota cada elemento da lista(). >>>> (1, 2, 3, 4, 5)
# # o argumento sep='' é um separador da função print()!!!! você define o que sepaara os elementos.

########################################################

# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5,6]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2) # desempacota as listas dentro do *args.
# #(saída >>>>> (1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50) )

###########################################################
def func(*args, **kwargs): # kwargs coloca a saída com um dic() de Chave e Valor.
    print(args)
    print(kwargs) # printa key and value
    print(kwargs['nome'], kwargs['sobrenome']) # printa os valores da chaves!!!

    nome = kwargs.get('nome') # get procura se entre os elementos houve alguma chave nomeada com 'nome'.
    print(nome)

    idade = kwargs.get('idade') # get procura e se encontrar mostra a idade, senão, mostra 'Idade não existe',
    # evitando assim a saída 'None' referente a .get
    if idade is not None:
        print(idade)

    else:
        print('Idade não existe')


lista = [1,2,3,4,5,6]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='JOSE', sobrenome='ALEXANDRE', idade='34')
# desempacota as listas dentro do *args, mas não mostra os argumentos de **kwargs.

#(saída do print(args >>>>> (1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50) )
#(saída do print(kwargs >>>>> {'nome': 'JOSE', 'sobrenome': 'ALEXANDRE'})