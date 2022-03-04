# Escreva um algoritmo que elia um número inteiro qualauqr e peça para o usúario escolher qual será a base de conversão

num = int(input('Dígite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} converttido para Binário é igual a {}'.format(num, bin(num)[2:])) # [2:] não irá mostrar os 2 primeiros números
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')