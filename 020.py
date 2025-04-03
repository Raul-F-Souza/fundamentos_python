'''
Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.
'''

peso = float(input('Digite seu peso: '))
idade = int(input('Digite sua idade: '))

if idade >= 16 and idade <= 69 and peso >= 50:
    print('Você pode doar sangue')
else:
    print('Você não pode doar sangue')    