# Algoritmo para ler seis números inteiros e mostrar a soma só dos números pares. E ignorar os números ímpares

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Dígite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))