# variavel = 'valor'
#
# def func():
#     print(variavel)
#
# def func2():
#     global variavel
#     variavel = 'Outro valor'
#     print(variavel)
#
#
# func()
# func2()
# print(variavel)
########################################################
# variavel = 'Jose Alexandre da Silva Junior'
#
# def func():
#     print(variavel)
#
# def func2(arg=None):
#     arg = arg.replace('v', 'c')
#     arg = arg.replace('a', 'k')
#     return arg
#
#
# func()
# outra_variavel = func2(arg=variavel)
# print(outra_variavel)

####################################################

# não está usando uma variável global, apenas variáveis locais no suite das funções.
def func():
    outra_variavel = 'Luiz Otavio'
    return outra_variavel

def func2(arg):
    print(arg)

var = func() # essa variável recebe o valor de returno da func() --- 'Luiz Otávio' --
func2(var) # essa função mostra como argumento o valor returnardo e armazenado na variavel var







