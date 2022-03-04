# A confederaçaõ Nacional De Natação precisa de um programa para ler o ano de nascimento de um atleta e mostre sua categoria

from datetime import date # comando para importar o ano atual
atual = date.today().year # comando para pegar o ano atual
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem \033[0;33m{}\033[m anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[0;33mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[0;33mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[0;33mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[0;33mSÊNIOR\033[m')
else:
    print('Classificação: \033[0;33mMASTER\033[m')