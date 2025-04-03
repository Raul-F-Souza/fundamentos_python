'''
Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000
'''

resposta = int(input('Digite o número para mostrar sua tabuada \n[0000 p/ Sair]:'))
contador = 0

while True:
    
    if resposta == 0000:
        print('Até logo! :)')
        break
    elif contador < 10:
        contador += 1
        print(f'{resposta} X {contador} = {resposta * contador}')
    else:
        contador = 0
        print('-' * 20)
        resposta = int(input('Digite o número para mostrar sua tabuada \n[0000 p/ Sair]:'))
        print('-' * 20)