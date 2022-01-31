# nome = input('Qual é o seu nome? ')

# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada =(')
# print(nome or 'Você não digitou nada =(') # se nome tiver um valor, diferente de vazio, se não mostra a segunda expr.
# print(nome or None or False or 0 or 'Você não digitou nada =(')

a = 0
b = None
c = False
d = []
e = {}
f = ()
g = 34
h = 'JOSE'

variavel = a or b or c or d or e or f or g or h
print(variavel)