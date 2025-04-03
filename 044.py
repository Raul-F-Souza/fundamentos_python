'''
Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias
'''

import random
import time

pc = random.randint(1, 3)
j = int(input(f'1 - Pedra\n'
              f'2 - Papel\n'
              f'3 - Tesoura ----> '))
vitorias = 0

while True:
    print('JO')
    time.sleep(1)
    print('KEM')
    time.sleep(1)
    print('PO')
    time.sleep(1)
    print('Ainda pensando...')
    time.sleep(1)

    if pc == j:
        print('Empate')
        j = int(input(f'1 - Pedra\n'
                      f'2 - Papel\n'
                      f'3 - Tesoura ----> '))
        
    elif ((j == 1 and pc == 3) or
        (j == 2 and pc == 1) or
        (j == 3 and pc == 2)):
        print(f'Ganhou! {j} X {pc} :)')
        
        vitorias += 1
        
        j = int(input(f'1 - Pedra\n'
                      f'2 - Papel\n'
                      f'3 - Tesoura ----> '))
    else:
        print(f'Perdeu! {j} X {pc}'
              f'\nVocê ganhou {vitorias} vezes!')
        break