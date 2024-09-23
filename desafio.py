import os

MAX_CARACTERES = 45
MSG_CONTINUAR = '\n\nAperte enter para continuar...'
MSG_DEPOSITO_SUCESSO = '\nDepósito realizado com sucesso!'
MSG_SAQUE_SUCESSO = '\nSaque realizado com sucesso!'
MSG_FALHA_VALOR_INVALIDO = '\nOperação falhou! O valor informado é inválido.'
MSG_FALHA_SALDO_INSUFICIENTE = '\nOperação falhou! Você não tem saldo suficiente.'
MSG_FALHA_LIMITE_SAQUE_DIARIO = '\nOperação falhou! Número máximo de saques excedido.'
MSG_FALHA_VALOR_LIMITE_SAQUE = '\nOperação falhou! O valor do saque excede o limite.'

VALOR_LIMITE_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3

saldo = 0
extrato = ""
numero_saques = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(titulo):
    return f' {titulo} '.center(MAX_CARACTERES, '=') + '\n'

def menu():
    clear()
    menu = cabecalho('BANCO PYTHON')
    menu += cabecalho('MENU')
    menu += """
    O que você deseja fazer?

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    Escolha: """

    return menu

def depositar():
    clear()
    msg = cabecalho('BANCO PYTHON')
    msg += cabecalho("DEPÓSITO")
    msg += "\nInforme o valor para depósito: "
    return msg

def sacar():
    clear()
    msg = cabecalho('BANCO PYTHON')
    msg += cabecalho("DEPÓSITO")
    msg += "\nInforme o valor para saque: "
    return msg

def get_extrato():
    clear()
    msg = cabecalho('BANCO PYTHON')
    msg += cabecalho("EXTRATO")

    if(extrato):
        msg += extrato
        msg += "".center(MAX_CARACTERES,'-')
        espacamento = MAX_CARACTERES + 1 - len('R$ ') - len(f"{saldo:.2f}")  
        msg += '\nSaldo'.ljust(espacamento) + f'R$ {saldo:.2f}\n'
        msg += "".center(MAX_CARACTERES,'-')
    else:
        msg += "\nNão foram realizadas movimentações."
        
    msg += '\n\nAperte enter para continuar... '
    return msg



while True:

    opcao = input(menu()).lower()

    if opcao == "d":
        valor = float(input(depositar()))

        if valor > 0:
            saldo += valor
            espacamento = MAX_CARACTERES - len('R$ ') - len(f"{valor:.2f}")  
            extrato += 'Depósito'.ljust(espacamento) + f'R$ {valor:.2f}\n'
            print(MSG_DEPOSITO_SUCESSO)

        else:
            print(MSG_FALHA_VALOR_INVALIDO)
        
        input(MSG_CONTINUAR)

    elif opcao == "s":
        valor = float(input(sacar()))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > VALOR_LIMITE_SAQUE

        excedeu_saques = numero_saques >= LIMITE_SAQUE_DIARIO

        if excedeu_saldo:
            print(MSG_FALHA_SALDO_INSUFICIENTE)

        elif excedeu_limite:
            print(MSG_FALHA_VALOR_LIMITE_SAQUE)

        elif excedeu_saques:
            print(MSG_FALHA_LIMITE_SAQUE_DIARIO)

        elif valor > 0:
            saldo -= valor
            espacamento = MAX_CARACTERES - len('R$ ') - len(f"{valor:.2f}")  
            extrato += 'Saque'.ljust(espacamento) + f'R$ {valor:.2f}\n'
            numero_saques += 1
            print(MSG_SAQUE_SUCESSO)

        else:
            print(MSG_FALHA_VALOR_INVALIDO)
        
        input(MSG_CONTINUAR)

    elif opcao == "e":
        input(get_extrato())

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")