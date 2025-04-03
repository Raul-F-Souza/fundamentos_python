# Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
'''
V = (4/3) . π . r³
A = 4 . π . r²
'''

# Entrada de dados
r = float(input('Digite o raio de uma esfera: '))

# Cálculos internos
v = (4/3) * 3.1415 * (r ** 3)
a = 4 * 3.1415 * (r ** 2)

# Saída de dados
print(f'Volume da esfera: {v:.2f}\nÁrea da esfera: {a:.2f}')