'''
Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
n5 = float(input('Digite a quinta nota: '))

media = (n1 + n2 + n3 + n4 + n5) / 5

if media < 6:
    print(f'Média insuficiente!')
elif media >= 6 