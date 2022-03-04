# Algoritmo para calcular a soma entre todos os números ímpares que são Mútiplos de Três

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
        print(c, end=' ') # números diviziveis por três
print('\nA soma de todos os \33[1;31m{}\033[m valores solicitados é \033[1;32m{}\033[m'.format(cont, soma))
