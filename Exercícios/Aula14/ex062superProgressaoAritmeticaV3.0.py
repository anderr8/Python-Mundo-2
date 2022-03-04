# Melhore o desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos.
# O programa deve encerrar com o número 0 termo.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeio termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print ('{} → '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com \033[2;32m{}\033[m termos mostrados.'.format(total))