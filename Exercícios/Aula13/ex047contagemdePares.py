# Algoritmo para para mostrar os números Pares

# Primeiro exemplo:
'''for n in range(1, 51):
    print('.', end='')
    if n % 2 ==0:
        print(n, end=' ')
print('\033[4;31mEsses são os números Pares.\033[m')'''

for n in range(2, 51, 2):
    #print('.', end='')
    print(n, end=' ')
print('Esses são os números Pares.')