'''
Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.
'''
import random

tentativa = 0
num_tentativa = 0
num = random.randint(1, 10)

while num_tentativa != num:
    num_tentativa = int(input('Tente adivinhar um número de 1 a 10: '))
    tentativa += 1

    print(f'------------------------------'
          f'\nQuase!'
          f'\nO número era {num}')

print('Você conseguiu')
print(f'Número de tentativas: {tentativa}')