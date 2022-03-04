# Algoritmo para ler 2 números inteiros e compara-los se são maoires, menores ou iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O Primeiro valor é maior.')
elif n2 > n1:
    print('O Segundo valor é maior.')
else:
    print('Os dois números são iguais.')