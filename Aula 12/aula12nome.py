nome = str(input('Qual é o seu nome? '))
if nome == 'Anderson':  # Quando é usado só o if é chamada de estrutura condicional simplpes
    print('Que nome bonito!')
    #print('Tenha um lindo dia, \033[1;32m{}\033[m!'.format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': # Quando usado if, elif e else é chamada de condição aninhada
elif nome in 'Ana Cládia Jéssica Juliana':
    print('Belo nome feminino')
    print('Seu nome é bem popular no Brasil.')
else: # Quando é usado com o else é chamada de estrutura condicional composta
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[4;31m{}\033[m!'.format(nome))