menu = '''
---------------------------------------------

            MENU BANCARIO
[1] Depositar
[2] Sacar
[3] Extrato
[0] Exit
--------------------------------------------
'''


deposito = 0
saldo = 0
limite = 500
saque=0
LIMITE_SAQUE = 3
numero_saque = 0
extrato =""

while True:
    opcao = input(menu)

    if(opcao == "1"):
        
        deposito = float (input("\nInforme o valor que deseja depositar: "))

        if(deposito >= 0):  
           saldo = saldo + deposito
           print(f"Deposito de {deposito} foi realizado com sucesso")
           extrato += f"Deposito: R$ {deposito:.2f}\n"

        else:
            print("Erro, o valor depositado não é valido")

    elif(opcao == "2"):
        
        saque = float(input("\nInforme o valor que deseja sacar: "))

  

        excedeu_saldo = saque > saldo
        execedeu_limite = saque > limite
        execedeu_saque =  numero_saque >= LIMITE_SAQUE

        if(excedeu_saldo):
            print("Opereção falhou, saldo insuficiente.")

        elif(execedeu_limite):
            print("Opereção falhou, limite de saque ultrapassado.")

        elif(execedeu_saque):
            print("Opereção falhou, quantidade de saques atingida.")
        
        elif (saque > 0):
            saldo -= saque
            numero_saque +=  1
            extrato += f"Saque: R$ {saque:.2f}\n"  
        else:
            print("Valor de saque invalido, digite valor valido.")

            
    elif(opcao == "3"):
        print("\n####### Extrato Bancario ####### ")
        print("\nNão foram realizadas movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#####################################")
    elif(opcao == "0"):
        break
    else:
        print(" Numero invalido, digite um numero valido ")
