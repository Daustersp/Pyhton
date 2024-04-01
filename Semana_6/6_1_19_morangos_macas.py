import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira a quantidade de morangos e maçãs adquiridas
quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

# Calcula o preço dos morangos
if quantidade_morangos <= 5:
    preco_morangos = quantidade_morangos * 2.50
else:
    preco_morangos = quantidade_morangos * 2.20

# Calcula o preço das maçãs
if quantidade_macas <= 5:
    preco_macas = quantidade_macas * 1.80
else:
    preco_macas = quantidade_macas * 1.50

# Calcula o total sem desconto
total_sem_desconto = preco_morangos + preco_macas

# Verifica se o cliente tem direito ao desconto
if quantidade_morangos + quantidade_macas > 8 or total_sem_desconto > 25:
    desconto = total_sem_desconto * 0.10
else:
    desconto = 0

# Calcula o total com desconto
total_com_desconto = total_sem_desconto - desconto

# Exibe o valor a ser pago pelo cliente
print(f"O valor a ser pago pelo cliente é: R$ {total_com_desconto:.2f}")