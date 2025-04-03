'''
Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).
'''

num = int(input(f'1. Segunda-feira\n'
                f'2. Terça-feira\n'
                f'3. Quarta-feira\n'
                f'4. Quinta-feira\n'
                f'5. Sexta-feira\n'
                f'6. Sábado\n'
                f'7. Domingo\n'
                f'----> '))

if num == 1:
    print('Segunda-feira!')
elif num == 2:
    print('Terça-feira!')
elif num == 3:
    print('Quarta-feira!')
elif num == 4:
    print('Quinta-feira!')
elif num == 5:
    print('Sexta-feira!')
elif num == 6:
    print('Sábado-feira!')
elif num == 7:
    print('Domingo!')
else:
    print('Erro')