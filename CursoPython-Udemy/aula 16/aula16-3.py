"""
Faça um programa que peça o primeiro nome do usuáruio. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = str(input('Digite o seu primeiro nome: ')).strip().upper()

if len(nome) <= 4:
    print(f'Seu nome tem {len(nome)} letras e é curto.')
elif len(nome) >=5 and len(nome) <=6:
    print(f'Seu nome tem {len(nome)} letras e é normal')
else:
    print(f'Seu nome tem {len(nome)} letras e é muito grande!')