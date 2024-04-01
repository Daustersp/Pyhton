import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Define os preços dos combustíveis
preco_gasolina = 3.30
preco_alcool = 2.90

# Solicita ao usuário que insira o número de litros vendidos e o tipo de combustível
litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()

# Calcula o valor a ser pago pelo cliente
if tipo_combustivel == 'A':
    valor_total = litros_vendidos * preco_alcool
elif tipo_combustivel == 'G':
    valor_total = litros_vendidos * preco_gasolina
else:
    print("Tipo de combustível inválido.")
    exit()

# Exibe o valor total a ser pago pelo cliente
print(f"O valor total a ser pago pelo cliente é: R$ {valor_total:.2f}")