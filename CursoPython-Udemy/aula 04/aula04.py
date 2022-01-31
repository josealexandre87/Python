"""
Tipos de Dados
str - string - texto 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -30 -60 -1500 1500
float - real/ponto flutuante - -10.50 1.5 -10.10 -50.93 0.0
bool - boleano/lógico - True/False 10 == 10 (True), 10 == 100 (False)

"""
#Strings
print('JOSE', type('JOSE')) # JOSE <class 'str'>
print('10', type('10')) # 10 <class 'str'>
#Inteiros
print(10, type(10)) # 10 <class 'int'>
#Real/Ponto Flutuante
print(25.23, type(25.23)) # 25.23 <class 'float'>
#caso do zero(0)
print(0.0, type(0.0)) # 0.0 <class 'float'>
print(0, type(0)) # 0 <class 'int'>
#Boleanos (True/False)
print(10 == 10, type(10 == 10)) # True <class 'bool'>
print('l' == 'l', type('l' == 'l')) # True <class 'bool'>
print('L' == 'l', type('L' == 'l')) # False <class 'bool'>

#avaliados em False
print(bool("")) # False
print(bool([])) # False
print(bool(0)) # False


#Type Casting em Python (converter o tipo)
print('JOSE', type('JOSE'), bool('JOSE')) #JOSE <class 'str'> True -----> avaliou JOSE como Verdadeiro (True)
print('10', type('10'), type(int('10'))) # 10 <class 'str'> <class 'int'>
print('Luiz', float('10.5')) #Luiz 10.5

print(10+10)
#print('10'+10) # não pode TypeError

#String: nome
print('JOSE ALEXANDRE', type('JOSE ALEXANDRE')) #JOSE ALEXANDRE <class 'str'>

#Idade: int
print(34, type(34)) #34 <class 'int'>

#Altura: float
print(1.90, type(1.90)) #1.9 <class 'float'>

# É maior de idade vc > 18
print(34 > 18 ), type(34 > 18) #True

