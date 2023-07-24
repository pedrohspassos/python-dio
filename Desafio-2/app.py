# separar funções saque, deposito e extrato 
# e criar duas funções: cadastro usuario e cadastro conta banco


 
def menu():
    menu = '''
    ---------------------------------------------

                MENU BANCARIO
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Exibir contas
    [6] Novo usuario
    [0] Exit
    --------------------------------------------
    ''' 
    return input(menu)

def depositar(saldo ,deposito, extrato, /):
    
    if(deposito >= 0):  
           saldo = saldo + deposito
           print(f"Deposito de {deposito} foi realizado com sucesso")
           extrato += f"Deposito: R$ {deposito:.2f}\n"

    else:
        print("!! Erro, o valor depositado não é valido !!")

    return saldo, extrato


def sacar(*,saldo, saque, extrato, limite, numero_saques, limite_saques):
    
        excedeu_saldo = saque > saldo
        execedeu_limite = saque > limite
        execedeu_saque =  numero_saques >= limite_saques

        if(excedeu_saldo):
            print("Opereção falhou, saldo insuficiente.")

        elif(execedeu_limite):
            print("Opereção falhou, limite de saque ultrapassado.")

        elif(execedeu_saque):
            print("Opereção falhou, quantidade de saques atingida.")
        
        elif (saque > 0):
            saldo -= saque
            numero_saques +=  1
            extrato += f"Saque: R$ {saque:.2f}\n"  
            print("Saque realizado")
        else:
            print("Valor de saque invalido, digite valor valido.")
        
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    
        print("\n####### Extrato Bancario ####### ")
        print("\nNão foram realizadas movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#####################################")

def criar_usuario(usuarios):
     cpf = input("Insira o CPF (apenas numeros): ")
     usuario = filtar_usuario(cpf, usuarios)

     if usuario:
          print("Já existe usuario com esse CPF")
          return 
     
     nome = input("Insira o nome completo: ")
     data_nasc = input("Insira a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Insira o endereco (logradrouro, nro - bairro - cidade/sigla estado): ")

     usuarios.append({"nome": nome,"data_nascimento": data_nasc, "cpf":cpf ,"endereco": endereco})
     
     print("Usuario cadastrado com sucesso")

def filtar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, num_conta, usuarios):
     cpf = input("Insira o CPF (apenas numeros): ")
     usuario = filtar_usuario(cpf, usuarios)

     if usuario:
          print("Conta criada com sucesso")
          return {"agencia":agencia, "numero_conta": num_conta, "usuario":usuarios}

     print("Usuario não encontrado")


def listar_contas(contas):
     for conta in contas:
          texto = f"""

              Agência: {conta["agencia"]}
              C/C: {conta["numero_conta"]}
              Titular:{conta["usuario"]["nome"]}

          """
     

def main():
       
  LIMITE_SAQUE = 3
  AGENCIA =  "0001"

  deposito = 0
  saldo = 0
  limite = 500
  saque=0
  numero_saque = 0
  extrato =""
  usuarios=[]
  contas=[]


  while True:
      opcao = menu()

      if(opcao == "1"):
          deposito = float (input("\nInforme o valor que deseja depositar: "))

          saldo, extrato = depositar(saldo, deposito, extrato)

      elif(opcao == "2"):
          saque = float(input("\nInforme o valor que deseja sacar: "))

          saldo, extrato = sacar(
              saldo= saldo,
              saque= saque,
              extrato=extrato,
              limite= limite,
              numero_saques=numero_saque,
              limite_saques=LIMITE_SAQUE,

          )
                
      elif(opcao == "3"):
          exibir_extrato(saldo, extrato= extrato)
      
      elif(opcao == "4"):
          criar_usuario(usuarios)
          
      elif(opcao == "5"):
          numero_conta = len(contas) + 1
          conta=criar_conta(AGENCIA, numero_conta, usuarios)

          if conta:
                contas.append(conta)
                
      elif(opcao == "6"):
          listar_contas(contas)

      elif(opcao == "0"):
          break
      else:
          print(" Numero invalido, digite um numero valido ")



main()