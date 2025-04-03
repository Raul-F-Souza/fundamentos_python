'''
Escreva um programa que verifique se uma palavra é um palíndromo.
'''

palavra = input('Digite uma palavra: ').upper().strip()
pontos = 0

if palavra == palavra[::-1]:
    print('é palindromo')
else:
    print('não é')

'''
for x in range(0, len(palavra)):
    if palavra[x] == palavra[-x -1]:
        pontos = pontos + 1

if pontos == len(palavra):
    print('é um palindromo')
else:
    print('não é')
'''