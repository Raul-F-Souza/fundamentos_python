# Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome = input('Digite seu nome: ')

print(f'Primeiro nome: {nome[:nome.find(' ')]}\n'
      f'Último nome: {nome[nome.rfind(' ') + 1:]}')