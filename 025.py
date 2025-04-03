import time
import random

pc = random.randint(1, 3)
j = int(input(f'1 - Pedra\n'
              f'2 - Papel\n'
              f'3 - Tesoura ---->'))

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
elif ((j == 1 and pc == 3) or
     (j == 2 and pc == 1) or
     (j == 3 and pc == 2)):
    print(f'Ganhou! {j} X {pc}')
else:
    print(f'Perdeu! {j} X {pc}')