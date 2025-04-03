#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico,
#permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair

resposta = 0
saldo = 0

while resposta != 4:
    resposta = int(input('1. Deposito'
                     '\n2. Saque'
                     '\n3. saldo'
                     '\n4. Sair ----> '))

    if resposta == 1:
        deposito = float(input('Digite quanto quer depositar: '))
        saldo += deposito
    elif resposta == 2:
        saque = float(input('Digite quanto quer sacar: '))
        saldo -= saque
    elif resposta == 3:
        print(f'Seu saldo é {saldo}')
    elif resposta == 4:
        print('Até logo!')
    else:
        print('Opção invalida')