#Variáveis do sistema
saldo = 0
registro_deposito = []
registro_saque = []
variavel_laco = True
num_saques = 0
valor_limite_saque = 500
#------------

print("Bem vindo ao sistema bancario")

while variavel_laco:
    nome = int(input("""
    digite 1 para depositar
    digite 2 para sacar
    digite 3 para mostrar o extrato
    digite 0 para sair
    """))

    match nome:

        case 1: #Depósito
            valor_deposito = float(input("digite o valor do depósito: "))

            if valor_deposito > 0:
                saldo = saldo + valor_deposito
                registro_deposito.append(valor_deposito)

            else:
                print("Não é possível depositar esse valor!")

        case 2: #Saque
            if num_saques <3:
                valor_saque = float(input("digite o valor do saque: "))

                if valor_saque < valor_limite_saque and valor_saque < saldo:
                    saldo = saldo - valor_saque
                    valor_limite_saque -= valor_saque
                    registro_saque.append(valor_saque)
                    num_saques += 1

                elif valor_saque > valor_limite_saque:
                    print("Esse saque excede o valor do limite diário")

                else:
                    print("Limite insuficiente para realizar o saque!")

            else:
                print("Limite de saques alcançado")

        case 3:
            if len(registro_saque) == 0 and len(registro_deposito) ==0:
                print("Não foram realizadas movimentações")

            else:
                print("Depositos realizados:")
                for valor in registro_deposito:
                    print("R$: ", valor)

                print("Saques realizados:")

                for valor in registro_saque:
                    print("R$: ", valor)

                print("Saldo: ", saldo)

        case 0:
            variavel_laco = False

        case _:
            print("Comando inválido!")
