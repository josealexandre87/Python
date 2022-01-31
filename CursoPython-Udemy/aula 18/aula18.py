"""
Manipulando Strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
#positivos   [012345678]
texto      = 'Python s2'
# negativos -[987654321]

print(texto[8])
print(texto[6])
print(texto[3])
print(texto[-9])

url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[2:6]
print(nova_string)

nova_string2 = texto[:6]
print(nova_string2)

nova_string3 = texto[7:]
print(nova_string3)

nova_string4 = texto[0::2]
print(nova_string4)

print(len(texto))