'''n = s = 0
while True:
    n = int(input('Dígite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma {s}.') # exemplo papi string => f , tecnica de interpolação'''

nome = 'Anderson'
idade = 41
print(f'O {nome} tem {idade} anos.') # forma nova Phyton 3.6+
print('O {} tem {} anos.'. format(nome, idade)) # Phyton 3
print('O %s tem %d anos.'% (nome, idade)) # forma antiga Phyton 2

nome = 'Anderson'
idade = 41
salário = 7500.00
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}.')