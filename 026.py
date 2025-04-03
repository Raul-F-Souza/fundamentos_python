'''
Escreva um programa que calcule e classifique o IMC do usuário
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc > 25.5:
    print('Você está acima do peso')
elif imc > 18.6:
    print('Peso ideal')
else:
    print('Você está abaixo do peso')