import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira a descrição do produto, a quantidade adquirida e o preço unitário
descricao_produto = input("Digite a descrição do produto: ")
quantidade_adquirida = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

# Calcula o total
total = quantidade_adquirida * preco_unitario

# Calcula o desconto
if quantidade_adquirida <= 5:
    desconto = total * 0.02
elif quantidade_adquirida <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# Calcula o total a pagar
total_a_pagar = total - desconto

# Exibe o total, o desconto e o total a pagar
print(f"Descrição do produto: {descricao_produto}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")