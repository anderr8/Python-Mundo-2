# Melhore o jogo do Desafio 028 onde o Computador vai "Pensar" em um número entre 0 a 10.
# Agora vamos tentar adiviunhar e mostrar quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Sou seu compútador... Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com \033[4;32m{}\033[m tentativas. Parabéns!!!'.format(palpites))