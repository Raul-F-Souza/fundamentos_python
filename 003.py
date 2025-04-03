# Escreva um programa que leia o nome, e o sobrenome,
# CONCATENE em uma nova variável nome completo, e retorne para o usuário

# Entrada de dados
nome = input('Digite somente seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')

# Concatenação das variáveis
nome_completo = nome + ' ' + sobrenome # Adicionado string vazia para formatação do output

# Saída de dados
print(f'Seu nome completo é {nome_completo}')