'''
Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.
'''

num = int(input('Digite um número inteiro positivo: '))

if num <= 10 and num >= 0:
    print(f'O número {num} está entre 0 a 10')
elif num > 10 and num <= 20:
    print(f'O número {num} está entre 10 a 20')
elif num > 20:
    print(f'O número {num} é maior que 20')
else:
    print('Algo deu errado, digite novamente')