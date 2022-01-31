nome = 'Luiz'
idade = 32
altura = 1.80
e_maior = idade > 18
data_1 = True
data_atual = 2019
peso = 80
imc = peso/altura**2

print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc) #Luiz tem 32 anos de idade e seu imc é: 24.691358024691358
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}') #Luiz tem 32 anos de idade e seu imc é: 24.69
print('{} tem {} anos e seu imc é: {:.2f}'.format(nome, idade, imc)) #Luiz tem 32 anos e seu imc é: 24.69
print('{0} tem {1} anos e seu imc é: {2:.2f}'.format(nome, idade, imc)) #Luiz tem 32 anos e seu imc é: 24.69
print('{n} tem {i} anos e seu imc é: {im:.2f}'.format(n=nome, i=idade, im=imc)) #Luiz tem 32 anos e seu imc é: 24.69