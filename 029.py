'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.
'''

num = int(input('Digite um número: '))

for n in range(1, 11):
    print(f'{num} X {n} = {num * n}')