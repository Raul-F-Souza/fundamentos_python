'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1 O nome com todas as letras maiúsculas
2 O nome com todas minúsculas
3 Quantas letras ao todo (sem considerar os espaços)
4 Quantas letras tem o primeiro nome
'''

nome = input('Digite seu nome: ').strip()

print(f'Maiúsculo: {nome.upper()}\n'
      f'Minúscula: {nome.lower()}\n'
      f'Quantidade de caracteres: {len(nome) - nome.count(' ')}\n'
      f'Quantidade de letras no primeiro nome: {nome.find(' ')}')
      #f'primeiro nome: {len(nome[:nome.find(' ')])}')
