# Algoritmo para ler o ano de nascimento de um jovem e informar se é a hora de se alistar  ou se já passoudo tempode alistamento,
# e mostrar o tempo que falta para o prazo

sexo = int(input('''Qual o sexo: 
[1] masculino
[2] feminino
Opção:'''))
import sys
if sexo == 1:
    print('Pessoas do sexo masculino devem se alistar.')
else:
    sexo == 2
    print('Pessoas do sexo feminino não precisa se alistar.')
    sys.exit()
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem \033[1;33m{}\033[m anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar \033[1;31;43mIMEDIATAMENTE!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam \033[1;33m{}\033[m anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em \033[1;31m{}\033[m.'.format(ano))
elif idade > 18:
#else: -> opção no lugar do elif
    saldo = idade - 18
    print(' Você já deveria ter se alistado há \033[1;31m{}\033[m anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em \033[1;31m{}\033[m.'.format(ano))