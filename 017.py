'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.
'''

letra = input('Digite uma letra').upper()[0]

if letra in 'AEIOU':
    print('Vogal')
else:
    print('Consoante')