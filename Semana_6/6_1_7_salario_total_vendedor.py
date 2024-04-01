import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita o salário fixo e o valor das vendas efetuadas
salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
valor_vendas = float(input("Digite o valor das vendas efetuadas pelo vendedor: R$ "))

# Define o limite para o cálculo da comissão
limite_comissao = 1500

# Calcula a comissão
if valor_vendas <= limite_comissao:
    comissao = valor_vendas * 0.03  # 3% sobre o total das vendas
else:
    comissao = limite_comissao * 0.03 + (valor_vendas - limite_comissao) * 0.05  # 3% até R$ 1.500 e 5% sobre o que ultrapassar

# Calcula o salário total do vendedor
salario_total = salario_fixo + comissao

# Exibe o salário total do vendedor
print(f"O salário total do vendedor é: R$ {salario_total:.2f}")