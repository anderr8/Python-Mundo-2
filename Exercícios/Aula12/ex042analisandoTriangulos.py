# Algoritmo para anasisar Triângulos e mostrar se ele é Equilátero, Isósceles e Escaleno
'''Equilátero: todos os lados iguais
   Isósceles: dois lados iguais
   Escaleno: todos os lados diferentes'''

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento; '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FOORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('\033[1;34mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;34mESCALENO!\033[m')
    else:
        print('\033[1;34mISÓSCELES!\033[m')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')