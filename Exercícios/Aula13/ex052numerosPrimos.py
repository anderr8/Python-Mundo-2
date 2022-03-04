# Algoritmo que leia se o número é ou não Primo

núm = int(input('Dígite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível \033[33m{}\033[m vezes.'.format(núm, tot))
if tot == 2:
    print('E por isso ele é \033[33mPRIMO\033[m!')
else:
    print('E por isso ele não é \033[31mPRIMO\033[m!')