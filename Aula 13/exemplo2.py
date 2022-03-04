# Estrutura de repetição for

'''n = int(input('Dígite um número: '))
for c in range(0, n+1):# colocando +1 o número é contado até o número dígitado
    print(c)
print('FIM')'''

i = int(input('Início: '))
f = int(input('FIM: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

'''for c in range(0, 3): # nesse comando será perguntado para digitar 3 vezes um número
       n = int(input('Dígite um valor: '))
    print('fim')'''

'''s = 0
   for c in range(0, 4):
       n = int(input('Dígite um valor: '))
        s += n
   print('O somatório de todos os valores foi {}'.format(s)) '''