limite_valor_saque = 500
limite_diario_saque = 0
saldo = 0
extrato = ""

menu = """

# Banco DIO - Caixa eletronico #

[d] - Depósitos
[s] - Sacar
[e] - Extrato
[q] = Sair

=>"""

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso, retire o comprovante.")
        
        else:
            print("falha na operação valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Falha na operação, saldo insuficiente.")
        elif valor > limite_valor_saque or valor <= 0:
            print("Falha na operação, valor de saque não permitido.")
        elif limite_diario_saque >= 3:
            print("Falha na operação, limite diário de saque atingido.")
            
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            limite_diario_saque += 1
            print("Saque realizado com sucesso, retire o dinheiro.")
        
    elif opcao == "e":
        print ("\n##########  EXTRATO ##########")
        if not extrato:
            print ("\nNão houve movimentação")  
            print ("\n##############################")
        else:
            print(extrato)
            print (f"\nSaldo: R$ {saldo:.2f}")
            print ("\n##############################")
            
    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços.")
        break

    else:
        print("Opção inválida. Verifique e tecle novamente.")