'''
Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci
'''

n = int(input('Digite um número inteiro: '))
contador = 0
proximo = 0
atual = 1
anterior = 1

while contador < n:

    if contador == 0:
        print(0)
    elif contador == 1:
        print(1)
    elif contador == 2:
        print(1)
    else:
        # Inicio da regra geral para encontrarmos o próximo número em fatorial
        proximo = atual + anterior
        anterior = atual # Substituição para viabilizar sequencia
        atual = proximo # Substituição para viabilizar sequencia

        print(proximo)

    contador += 1