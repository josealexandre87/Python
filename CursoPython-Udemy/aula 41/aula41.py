"""
Dicionários
"""

d1 = {'chave_1': 'Valor da chave_1'}
d2 = dict(chave_2='Valor da chave_2')
d1['chave_1'] = 'Valor "na" chave_3'

print(d1, d2, sep='\n')
print(d1['chave_1'])

# CHAVES PRECISAM TER NOMES ÚNICOS!!!!!!!!

d_1 = {
    'str': 'valor',
    123: 'Outrovalor',
    (1,2,3,4,5): 'Tupla'
} # Posso usar qualquer valor imutável em chaves!!!

# Usar o modulo .get para acessar as chaves, pois não irá parar o código
# d_1.update({'nova_chave_update': 'valor_update'})
# print(d_1.get('str'))
# print(d_1)

# del d_1['str']

# print('str' in d_1)
# print('str' in d_1.keys())
# print('str' in d_1.values())
# print(d_1)
# print(len(d_1))
#
# for k in d_1:
#     print(k)
#
# for k in d_1.keys():
#     print(k)
#
# for v in d_1.values():
#     print(v)
#
# for k in d_1.items(): # mostra em tuplas
#     print(k[0], k[1])
#
# for k, v in d_1.items():
#     print(k, v, sep=' <-K:v-> ')

clientes = {
    'cliente1' : {
        'nome' : 'Jose',
        'sobrenome' : 'Alexandre da Silva Junior',
        'Idade' : 34,
    },
    'cliente2' : {
        'nome' : 'Rosi',
        'sobrenome' : 'Felipe da Silva',
        'Idade' : 38,
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibir {clientes_k}:')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

import copy

dic1 = {1 : 'a', 2: 'b', 3: 'c', 4: ['Jose', 'Alexandre']}
y = copy.deepcopy(dic1) #cópia profunda com o módulo importado copy
v = dic1.copy() #cópia rasa!!!!

v[1] = 'Jose'
v[4][0] = 'Arthur'

y[1] = 'Jose'
y[4][0] = 'Arthur'

print(dic1)
print(v)
print(y)

#juntar dicts

d1 = {
    1:2,
    2:4,
    3:6
}

d2 = {
    'a': 'b',
    'c':'d',
    'e':'f'
}

d1.update(d2) #update juta os dicionários. o sinal de + não concatena aqui.
print(d1)