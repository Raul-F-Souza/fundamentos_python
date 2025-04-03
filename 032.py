'''
Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um ´numero: '))

if n1 < n2:
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            print(i)
else:
    for i in range(n2, n1 + 1):
        if i % 2 == 0:
            print(i)