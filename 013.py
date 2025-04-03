'''
Crie um programa que leia uma frase e mostre:
1 Quantas vezes aparece a letra “a”
2 Em que posição ela aparece a primeira vez
3 Em que posição ela aparece na última vez
'''

frase = input('Digite uma frase: ')
frase_formatada = ((((frase.lower()).replace('ã', 'a')).replace('á', 'a')).replace('à', 'a')).replace('â', 'a')

print(f'Quantidade: {frase_formatada.count('a')}\n'
      f'Primeira posição: {frase_formatada.find('a') + 1}\n'
      f'Última posição: {frase_formatada.rfind('a') + 1}')