# Algoritmo para ler um número e mostrar o seu fatorial

'''Exemplo:
from math import factorial
n = int(input('Dígite um número para cálcular seu factorial: '))
f = factorial(n)
print('O factorial de {} é {}.'.format(n, f))'''

n = int(input('Dígite um número para cálcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))