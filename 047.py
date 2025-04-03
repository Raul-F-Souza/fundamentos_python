'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
'''

resposta = ''

while True:

    resposta = input('Deseja realizar um saque? [S/N]: ').strip().upper()[0]

    if resposta == 'N':
        print('Até logo! :)')
        break
    elif resposta == 'S':
        cedula_50 = 0
        cedula_20 = 0
        cedula_10 = 0
        cedula_1 = 0

        saque = int(input('Digite quanto deseja sacar: '))

        while saque > 0:
            if saque >= 50:
                saque -= 50
                cedula_50 += 1
    
            elif saque >= 20:
                saque -= 20
                cedula_20 += 1

            elif saque >= 10:
                saque -= 10
                cedula_10 += 1

            elif saque >= 1:
                saque -= 1
                cedula_1 += 1

        print(f'Cédulas de 50: {cedula_50}'
              f'\nCédulas de 20: {cedula_20}'
              f'\nCédulas de 10: {cedula_10}'
              f'\nCédulas de 1: {cedula_1}')
    else:
        print('Opção inválida')