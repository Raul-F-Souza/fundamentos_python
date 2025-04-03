'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final mostre:

A. Qual é o total gasto na compra
B. Quantos produtos custam mais de R$1000,00
C. Qual é o produto mais barato
'''

resposta = ''
total_gasto = 0.0
alto_valor = 0
valor_mais_barato = None
nome_mais_barato = None

while True:

    resposta = input('Quer adicionar um produto? [S/N]: ').strip().upper()[0]
    
    if resposta == 'N':
        print('-' * 35)
        break
    elif resposta == 'S':

        produto = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto [0.0]: '))
        total_gasto += preco
        if preco >= 1000:
            alto_valor += 1

        if valor_mais_barato == None and nome_mais_barato == None:
            valor_mais_barato = preco
            nome_mais_barato = produto

        if valor_mais_barato > preco:
            valor_mais_barato = preco
            nome_mais_barato = produto


    else:
        print('Opção inválida.')

    print('-' * 35)


print(f'Total gasto em produtos: {total_gasto:.2f}'
      f'\nQuantos custaram mais de 1000: {alto_valor}'
      f'\nO produto mais barato: {nome_mais_barato}')