"""
Pass e Ellipsis como placeholders
"""

valor = True

if valor:
    # Comentário   --- assim não é executado o que vir depois do # (tralha).
    print('Oi')
else:
    print('Tchau!')

################################################################################

valor = True

if valor:
    pass   # o Desenvolvedor deixa o PASS para posteriormente utilizar o espaço e inserir algum código.
           # O compilador pula para a próxima execução.
else:
    print('Tchau!')

################################################################################

valor = True

if valor:
    ...   # o Desenvolvedor também pode deixaa o ... (Ellipsis) e posteriormente utilizar o espaço.
           # O compilador pula para a próxima execução.
else:
    print('Tchau!')
