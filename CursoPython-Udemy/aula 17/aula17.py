"""
Formatando Valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ^)(QUANTIDADE) (Tipo - s, d ou f)

> ESQUERDA
< DIREITA
^ CENTRO
"""

num_1 = 10
num_2 = 3
divisao = num_1/num_2

print(f'{divisao:.2f}') #FString
print('{:.2f}'.format(divisao)) #Método .format

nome = 'jose'
print(f'{nome:s}')

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0^10}')

num_5 = 12345
print(f'{num_5:0>10.2f}')

nome2 = 'JOSE ALEXANDRE'
print(f'{nome2:#^50}')


#.format

nome3 = 'JOSE ALEXANDRE'
nome3_formatado = '{:@>50}'.format(nome3)
print(nome3_formatado)

#.format por declaração
nome4 = 'JOSE ALEXANDRE'
nome4_formatado = '{n:0<20}'.format(n=nome4)
print(nome4_formatado)

# .format por SEQUÊNCIA
nome5 = 'JOSE'
sobrenome = 'ALEXANDRE DA SILVA JUNIOR'
idade = 34
nome5_formatado = 'Meu nome é {} {} e eu tenho {} anos de idade.'.format(nome5, sobrenome, idade)
print(nome5_formatado)

# .format por INDICES!!!
nome6 = 'JOSE'
sobrenome = 'ALEXANDRE DA SILVA JUNIOR'
idade = 34
nome6_formatado = 'Meu nome é {2:0>10.2f} {1:#^5} e eu tenho {0:@<10} anos de idade.'.format(nome6, sobrenome, idade)
print(nome6_formatado)

nome7 = 'JOSE ALEXANDRE'
nome7 = nome7.ljust(30,'#') #justifica o nome a esquerda e completa com o caracter escolhido no parâmetro.
print(nome7)

nome8 = 'Jose Alexandre'
print(nome8.lower()) # Tudo minúsculo.
print(nome8.upper()) # Tudo maiúsculo.
print(nome8.title()) # Primeiras letras maiúsculas.