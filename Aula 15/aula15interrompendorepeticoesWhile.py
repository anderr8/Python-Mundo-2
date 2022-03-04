''' Comandos Break e loops infinitos '''


'''cont = 1
while cont <= 10: # para contar até 10
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

'''while True: -> comando para loop infinito
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''

# exemplo:
'''n = 0
while n != 999: # -> só para de contar quanto digitar 999, estrutura de repetição usando flag = ponto de parada
    n= int(input('Dígite um número: '))'''

# Exemplo:
'''n = cont = 0
while cont < 3: # -> para contar 3 números
    n = int(input('Dígite um número: '))
    cont += 1'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999 # gambiarra
print('A soma vale {}.'. format(s))'''

'''n = s = 0
while n != 999:
    n = int(input('Dígite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}.'. format(s))'''

