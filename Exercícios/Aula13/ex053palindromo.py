# Algoritmo para ler uma frse e mostrar se ela é um Palíndromo

# 1º exemplo:
'''frase = str(input('Dígite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palídromo!')
else:
    print('A frase digitada não é um Palíndromo!')'''

# 2º exemplo:
frase = str(input('Dígite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')
