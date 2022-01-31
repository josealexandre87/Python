"""
Operador Ternário em Python
"""

# logger_user = False
#
# msg = 'Usuário logado.' if logger_user else 'Usuário não está logado.' # operador ternário - escrito na mesma linha.
# # if logger_user: #== True: (mesma coisa de dizer que é verdade!!)
# #     msg = 'Usuário logado.'
# # else:
# #     msg = 'Usuário precisa logar.'
#
# print(msg)
###########################################################
# idade = 18
#
# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')

####################################

while True:
    idade = input('Qual é a sua idade? ')
    if not idade.isnumeric():
        print('Você precisa digitar somente números.')
    else:
        idade = int(idade)
        e_de_maior = (idade >= 18)
        msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'

        print(msg)

    flag = str(input('Você gostaria de parar o programa? [S ou N]' )).strip().upper()
    if flag == 'S':
        print('Vamos de novo!')
    else:
        print('Até Logo!')
        break
