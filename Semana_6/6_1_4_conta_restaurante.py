import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita o valor da refeição
valor_refeicao = float(input("Digite o valor da refeição: R$ "))

# Solicita a taxa de serviço (em porcentagem)
taxa_servico = float(input("Digite a taxa de serviço (%): "))

# Calcula o valor da taxa de serviço em reais
valor_taxa_servico = valor_refeicao * (taxa_servico / 100)

# Calcula o valor total a ser pago
total_a_pagar = valor_refeicao + valor_taxa_servico

# Exibe o valor total a ser pago
print(f"Valor total a ser pago: R$ {total_a_pagar:.2f}")