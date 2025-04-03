'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

1.A média de idade do grupo
2.Qual é o homem mais velho
3.Quantas mulheres têm menos de 20 anos

'''

soma_idades = 0
qt_mulheres_idade = 0
idade_homem_mais_velho = 0
homem_mais_velho = ''

for i in range(1, 5):
    nome = input("Digite seu nome: ").strip().lower()
    sexo = input("Digite seu sexo: ").strip().lower()
    idade = int(input("Digite sua idade: "))
    print('-' * 15)

    media = media + idade

    if sexo == "mulher" and idade < 20:
        qt_mulheres_idade = qt_mulheres_idade + 1

    if sexo == "homem" and idade < idade_homem_mais_velho:
            homem_mais_velho = nome

print(f'Média de idades: {soma_idades / 4} '
      f'\nHomem mais velho: {homem_mais_velho.capitalize()} '
      f'\nMulheres com 20 anos: {qt_mulheres_idade}')