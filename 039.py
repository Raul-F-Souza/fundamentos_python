'''
Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1
'''

num = int(input('Digite um número: '))
fatorial = 0
contador = 0

while contador < num:
    contador += 1
    fatorial += (num * contador)

    print(contador)

print(fatorial)