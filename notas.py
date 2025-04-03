# Operações Matematicas
'''
print(23 + 17) #Adição
print(12 - 144) #Subtração
print(25 / 255) #Divisão
print(6 * 125) #Multiplicação
print(12 ** 90) #Exponenciação
'''

# print com texo
'''
print('Olá mundo!!')
'''

# print formatado com texo + variável
'''
idade = 45
print(f'Minha idade é {idade}')
'''

# Leitura de dados
'''
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
print(f'Seu nome é {nome}, você tem {idade} anos')
'''

# Tipos de dados
'''
idade_1 = int(input('Digite a primeira idade: '))
idade_2 = int(input('Digite a segunda idade: '))
soma_idades = idade_1 + idade_2

print(f'A soma das idades é {soma_idades}')


# 22/02

# String
Senai = 'Luis Eulálio'

# Fatiamento
print(Senai[0])
print(Senai[3:7])
print(Senai[5])
print(Senai[7:])

# Análise
print(len(Senai))
print(Senai.count('l'))
print(Senai.find('l'))

print(Senai.lower())
print(Senai.upper())
print(Senai.replace('i', 'l'))
print(Senai)

nome = input('nome: ').strip()
print(nome)
'''

# WHILE

contador = 0

while contador < 5:
    print(contador)
    contador += 1

resposta = ''

while resposta != 'N':
    print(f'Bem vindo'
          f'\n[N] sair')
    resposta = input(':').strip().upper()[0]