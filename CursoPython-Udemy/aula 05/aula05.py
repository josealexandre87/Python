"""
+, -, *, /, //, **, %, ()

( n + n ) -> Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** -> Depois vem a exponenciação

*, /, //, % -> Na sequência multiplicação, divisão, divisão inteira e módulo

+, - -> Por fim, soma e subtração
"""

print('Multiplicação *', 10*10)
print('Adição +', 10 + 10)
print('Subtração -', 10 - 5)
print('Divisão /', 10 / 2)

print(10 * '10') # repetição de string
print(10 * 'A') # repetição de string
print('5' + '5') # concatenação (!!! não pode juntar int 10 + '10' str !!!) não concatena!!!!!!
print('JOSE' + ' ' + 'ALEXANDRE') # CONCATENA

print('Divisão inteira //', 10 // 3)
print('Divisão real /', 10 / 3)
print('Divisão do Modulo (resto) %', 10 % 3)

print('Precedencia ()', (5+2)*10, 5+2*10)