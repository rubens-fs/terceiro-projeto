nome = input('Qual é o seu nome? ')
print('É um prazer em te conhecer, {}!'.format(nome))
print('Escolha entre as opções abaixo:')
print('1 - Abrir Netflix 2 - Abrir Amazon Prime 3 - Abrir HBO GO 4 - Sair')
menu = int(input('Digite o número com a opção desejada: '))
print('{0} a opção que você escolheu foi a {1}!'.format(nome, menu))
if menu == 1:
    print('Ok! Abrir Netflix!')
elif menu == 2:
    print('Ok! Abrir Amazon Prime!')
elif menu == 3:
    print('Ok! Abrir HBO GO!')
elif menu == 4:
    print('Ok! Saindo do menu...')
else:
    print('Você deve escolher entre as opções 1, 2, 3 ou 4!')
