# Algoritmo que leia vários valores e só pare ao digitar 999 e, mostre quantos números
# foram digitados e a somas entre eles.

núm = cont = soma = 0
núm = int(input('Digite um número [99 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print('Você digitou \033[4;36m{}\033[m números e a soma entre eles foi \033[4;34m{}\033[m.'.format(cont, soma))