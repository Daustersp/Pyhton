import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira os dados da conta do cliente
numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo da conta: R$ "))
debito = float(input("Digite o débito da conta: R$ "))
credito = float(input("Digite o crédito da conta: R$ "))

# Calcula o saldo atual
saldo_atual = saldo - debito + credito

# Verifica se o saldo atual é positivo ou negativo
if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")

# Exibe o saldo atual
print(f"O saldo atual da conta {numero_conta} é: R$ {saldo_atual:.2f}")