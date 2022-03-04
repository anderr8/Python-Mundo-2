# Algoritmo para ler o ano de nascimento e mostrar quantas pessoas são menores de 21 anos e,quantas são
# maiores de de 21 anos

# Exemplo para mostrar se a pessoa é Maior ou Menor
'''from datetime import date
atual = date.today().year
nasc = int(input('Em que ano a pessoa nasceu? '))
idade = atual - nasc
print('Essa pessoa tem {} anos.'.format(idade))
if idade >= 21:
    print('Essa pessoa é maior de idade.')
else:
    print('Essa pessoa é menor de idade.')'''


# Exemplo para mostrar Sete Idade
'''from datetime import dat 
atual = date.today().year
for pess in range(1, 8):
    nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é maior.')
    else:
        print('Essa pessoa é menor.')'''


# Exemplo para mostrar quantas pessoas são Maiores e quantas pessoas são menores
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em qua ano {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E também tivemos {} pessoas menores de idade.'.format(totmenor))
