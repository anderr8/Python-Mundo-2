# refaça o desafio 051, lendo o termo e arazão de uma PA, mostrando os 10 primeiros termos usando a estrutura while

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')