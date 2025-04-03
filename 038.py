'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

opcao = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

while opcao != 5:
    print('---------------------')
    opcao = int(input(f'1. Somar'
                      f'\n2. Multiplicar'
                      f'\n3. Maior'
                      f'\n4. Novos números'
                      f'\n5. Sair do programa -----> '))
    print('---------------------')

    if opcao == 1:
        print(f'{n1} + {n2} + {n3} = {n1 + n2 + n3}\n')

    elif opcao == 2:
        print(f'{n1} X {n2} X {n3} = {n1 * n2 * n3}\n')

    elif opcao == 3:
        if n1 > n2 and n1 > n3:
            print(f'{n1} é o maior número\n')
        elif n2 > n1 and n2 > n3:
            print(f'{n2} é o maior número\n')
        elif n3 > n1 and n3 > n2:
            print(f'{n3} é o maior número\n')
        elif n1 == n2 and n2 == n3:
            print('Número iguais\n')

    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        n3 = int(input('Digite o terceiro número: '))

    elif opcao == 5:
        print('Até logo :)')
    else:
        print('Digito errado')