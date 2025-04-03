'''
Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000. No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''

soma = 0
contador = 0

while True:
    n = int(input('Digite um valor [0000 para sair]: '))
    contador += 1
    soma += n
    
    if n == 0000:
        break
    
print(f'Soma dos valores adcionados: {soma} \nForam digitados: {contador - 1} números ao total.')