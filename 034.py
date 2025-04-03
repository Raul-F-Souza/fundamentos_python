'''
Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma
'''

soma = 0

for i in range(0, 10):
    num = float(input(f"Digite o {i + 1}º número: "))
    if num % 2 == 0:
        soma = soma + num
        
print(soma)