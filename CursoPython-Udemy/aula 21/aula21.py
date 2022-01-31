"""
For in em Python
Iterando strings com for
Função range(star=0, stop, step=1)

"""
# texto = 'Python'
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1
#########################

# texto = 'Python'
#
# for letra in texto:
#     print(letra)
###########################
# texto = 'Python'
#
# for n, letra in enumerate(texto):
#     print(n, letra)
# texto = 'Python'
##############################
# for n in range(20, 10, -1):
#     print(n)
 ##################################
# for n in range(0, 100, 8):
#     print(n)
#
# print('$$$$$$$$$$$$$$$$$$$')
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        # continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)