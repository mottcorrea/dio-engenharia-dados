import os
os.system("cls")

menu = """

O que deseja fazer?

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        """
        - depositar apenas valores positivos
        - todos os depositos devem ser armazenados em variavel e exibidos no extrato
        """
        os.system("cls")
        print("\n================ DEPÓSITO ================")
        valor = float(input("Informe o valor do depósito: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            extrato += f"Depósito: R$ {valor:.2f}\n"
        print("=========================================")

    elif opcao == "s":
        print("SAQUE")
        """
        - apenas 3 saques diarios limite maximo de 500 reais por saque
        - caso nao tenha saldo em conta, deve ser exibida mensagem de erro
        - todos os saques devem ser armazenados em variavel e exibidos no extrato
        """
        os.system("cls")
        print("\n================ SAQUE ================")
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            print("=========================================")
            continue
        
        else:
            valor = float(input("Informe o valor do saque: "))

            if valor > saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif valor > limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif valor <= 0:
                print("Operação falhou! O valor informado é inválido.")
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

        print("=========================================")

    elif opcao == "e":
        """
        - deve listar todos os depositos e saques realizados
        - no fim da listagem deve ser exibido o saldo atual 
        - valores devem ser exibidos no formato R$ XXXX.XX
        """
        os.system("cls")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")
    
    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("OPÇÃO INVÁLIDA, POR FAVOR SELECIONE NOVAMENTE A OPERAÇÃO DESEJADA.")