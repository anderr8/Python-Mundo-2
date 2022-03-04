# Algorritmo pra calcular o IMC de um Pessoa e clasifica-lá

peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso /(altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABNÉS!, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em \033[4;33mSOBREPESO!\033[m')
elif 30 <= imc < 40:
    print('VOcê está em \033[4;31mOBESIDADE!\033[m')
elif imc >= 40:
    print('Você está em \033[4;31;40mOBESIDADE MÓRBIDA\033[m, \033[1;33mcuidado!\033[m')