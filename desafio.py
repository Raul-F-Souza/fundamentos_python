# Escreva um programa que execute o cálculo da Função horária da posição no MRUV,
# e retorne de acordo com o tempo informado pelo usuário

# Entrada de dados
t = int(input('Digite o tempo (em segundos) de deslocamento do objeto: '))
posicao_inicial = int(input('Digite a posição inicial do objeto: '))
velocidade_inicial = int(input('Digite a velocidade (km/h) inicial do objeto: '))
acerelacao= int(input('Digite a acelaração do objeto: '))

# Cálculo interno
s = posicao_inicial + (velocidade_inicial * t) + (acerelacao * (t ** 2))

# Saída de dados
print(f'A posição do objeto no tempo {t} é de {s} (m)')