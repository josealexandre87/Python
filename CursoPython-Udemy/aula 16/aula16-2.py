"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input('Qua horas são? '))

while True:
    try:
        if 0 <= hora <= 11:
            print('Bom Dia!')
        elif 12 <= hora <= 17:
            print('Boa Tarde!')
        elif 18 <= hora <= 23:
            print('Boa Noite!')
        break
    except:
        print('Digite outra hora.')
