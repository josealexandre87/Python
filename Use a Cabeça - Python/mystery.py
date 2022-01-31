
def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

#ARGUMENTO POR VALOR!!! (Faz uma cópia do valor que está na variável, mas a altera.)
# num = 10
# double(num)
# print(num)
#
# saying = 'Hello '
# double(saying)
# print(saying)
#
# numbers = [42, 256, 16]
# double(numbers)
# print(numbers)

#ARGUMENTO POR REFERÊNCIA!!! (Faz um 'link' com a variável e caso mude o valor na função, muda também o valor
#da variável referênciada.)

numbers = [42, 256, 16]
change(numbers)
print(numbers)