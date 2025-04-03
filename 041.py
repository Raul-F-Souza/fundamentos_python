'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''

resposta = ''
soma = 0
contador = 0
maior = None
menor = None

while resposta != 'N':
    n = int(input('Digite um número: '))

    soma += n
    contador += 1

    if maior == None and menor == None:
        maior = n
        menor = n

    if n > maior:
        maior = n

    if n < menor:
        menor = n

    resposta = input('Deseja continuar? [S/N]\n').strip().upper()[0]

print(f'A média dos valores é {soma/contador}'
      f'\nO maior número é {maior}'
      f'\nO menor é {menor}')