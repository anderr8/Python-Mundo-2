#  Algoritmo para ler o sexo de várias pessoas. Perguntar se o usuário quer ou não continuar.
#  E no final mostrar:
#  A) quantas pessoas tem mais de 18 anos.
#  B) quantos homens foram cadastrados.
#  C) quantas mulheres tem menos de 20 anos.

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homen(s) cadastrados.')
print(f'E temos {totM20} mulhere(s) com menos de 20 anos.')
