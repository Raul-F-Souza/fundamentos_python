'''
Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos
'''

maior_peso = None
menor_peso = None

for i in range(7):
    peso = float(input('Digite seu peso: '))

    '''
    aux_peso = peso

    if peso > maior_peso:
        maior_peso = peso
    elif aux_peso < peso:
        menor_peso = peso
    '''
    if maior_peso == None and menor_peso == None:
        maior_peso = peso
        menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

print(f'Maior peso: {maior_peso} \nMenor peso: {menor_peso}')