# Programa que leia vários valores inteiros, que pare quando digitar 999 -> flag, e mostre quantos números
# foram digitados e qual foi a soma.

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!.')