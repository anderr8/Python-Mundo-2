# Estrutura de Repetiçaõ While

# Exemplo 1:
'''for c in range(1, 10):
    print(c)
print('Fim')'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

# Exemplo 2:
'''for c in range(1, 5):
    n = int(input('Dígite um valor: '))
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Dígite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Dígite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

# Exemplo:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Dígite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares!'.format(par, impar))