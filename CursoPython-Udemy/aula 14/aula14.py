
'''
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False

'''

'''
num1 = input('Digite um númeo: ')
num2 = input('Digite outro número: ')

#isnumeric insdigit isdecimal

#num1 = int(num1)
#num2 = int(num2)

#print(num1 + num2)
print(num1.isnumeric())
print(num2.isnumeric())
'''
'''
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os números para realizar a conta.')
'''
num1 = input('Digite um númeo: ')
num2 = input('Digite outro número: ')

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print("ERROR")