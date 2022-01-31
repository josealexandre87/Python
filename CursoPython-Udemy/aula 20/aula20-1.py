"""

while / else
contadores
acumuladores

"""

contador = 1
acumulador = 1
while contador <= 10:
    print(contador, acumulador)

    if contador > 5:    # quebra o while e não executa o Else. Mas o print que está fora do while é executado sempre.
        break

    acumulador += contador
    contador += 1
else:
    print('Cheguei no Else.')   # se a condição do while for quebrada(break) p Else não é executado.
print('Cheguei no fim.')