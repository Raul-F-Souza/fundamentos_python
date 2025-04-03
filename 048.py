'''
Crie um programa que pede ao usuário para digitar dois números e, em seguida, divida o primeiro número pelo segundo número.
No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.

ZeroDivisionError ; ValueError
'''

resposta = ''

while True:

    print('-'* 35)
    resposta = input('Deseja realizar uma conta? [S/N]: ').strip().upper()[0]

    if resposta == 'N':
        print('Até logo! :)')
        break
    elif resposta == 'S':
        try:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))

            print(f'Resultado: {n1 / n2}')
        except ZeroDivisionError:
            print('0 não pode dividir um número')
        except ValueError:
            print('Utilize apenas números inteiros')
    else:
        print('Resposta inválida!'
              '\nTente Novamente\n')