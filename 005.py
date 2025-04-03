# Escreva um programa que converta real para o Franco Congolês

# Entrada de dados
real = float(input("Digite o valor em real para conversão: "))

# Definição de variável
franco_congoles = 499.45

# Saída de dados
print(f'{real} reais, equivalem a ${franco_congoles * real:.2f} Francos Congoleses') # ".2F" é a formatação que limita o número de casas decimais, sendo '2' a quantidade de casas