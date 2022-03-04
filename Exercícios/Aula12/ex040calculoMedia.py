# Algoritmo para calcular a média do aluno

nome = input('Qual o nome do aluno? ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('O aluno {}, tirando {:.1f} e {:.1f}, a média do é {:.1f}'.format(nome, nota1, nota2, média))
# exemplo => média >=5 and média < 7
if 7 > média >= 5:
    print('O aluno está em \033[4;33mRECUPERAÇÂO\033[m.')
elif média < 5:
    print('O aluno está \033[4;31mREPROVADO\033[m.')
elif média >= 7:
    print('O aluno está \033[4;34mAPROVADO!\033[m')