
import datetime

ano = int(input('Qual o seu ano de nascimento? '))
print(f'Você nasceu em {ano}.')

ano_hj = int(datetime.date.today().year)

if ano_hj - ano < 18:
    print('Você ainda vai se alistar ao serviço militar')
elif ano_hj - ano == 18:
    print('Hora de se alistar combatente!!')
else:
    print('Você passou do tempo para alistamento.')
print()
print('=*'*30)

# ANOTAÇÃO:
print(f'PARA TRANSFORMAR UMA DATA ANSI EM DATA DD/MM/AAAA: ')

from datetime import date

data_atual = date.today()
print(data_atual) # resultado -> 2018-03-01
data_em_texto = str(f'{data_atual.day}/{data_atual.month}/{data_atual.year}')
print(data_em_texto) # resultado -> 1/3/2018