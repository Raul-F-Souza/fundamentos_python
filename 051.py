'''
Crie uma função para verificar se um número é par ou ímpar
'''

def verificarNumeros(num):
    if num % 2 == 0:
        print(f'\nO número {num} é par')
    elif num % 2 != 0:
        print(f'\nO número {num} é ímpar')

while True:
    print('-'*35)
    resposta = input("Quer saber se um número é par ou ímpar? [S/N]: ").strip().upper()[0]

    if resposta == 'N':
        print('Até logo! :)')
        break
    elif resposta == 'S':
        verificarNumeros(int(input('Digite o número: ')))
    else:
        print(f'Opção "{resposta}" não identificada.'
              f'\nTente novamente.')