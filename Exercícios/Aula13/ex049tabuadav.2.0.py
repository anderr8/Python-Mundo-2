# Mostrando a Tabuada de um número qualquer

num = int(input('Dígite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))