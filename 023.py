'''
Escreva um programa que peça ao usuário uma palavra e imprima se começa com uma vogal ou consoante
'''

palavra = input('Digite uma palavra: ').strip().upper()[0]

if palavra in 'AEIOU':
    print('Vogal')
else:
    print('Consoante')