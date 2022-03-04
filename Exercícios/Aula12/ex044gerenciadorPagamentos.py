# Algoritmo para calcular o valor de pagamento de um produto, sendo à vista com desconto preço normal ou pecelado por 3x ou mais vezes
''' – à vista dinheiro/cheque: 10% de desconto
    – à vista no cartão: 5% de desconto
    – em até 2x no cartão: preço formal
    – 3x ou mais no cartão: 20% de juros'''


print('{:=^40}'.format('\033[1;31mLOJAS ANDERSON\033[m'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço *5 / 100)
elif opção == 3:
    total = preço
    parcela = total /2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$\033[1;33m{:.2f} COM JUROS\033[m.'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÂO ÍNVALIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R$\033[1;33m{:.2f}\033[m no final.'.format(preço, total))