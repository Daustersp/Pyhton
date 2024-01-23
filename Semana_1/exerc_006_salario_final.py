# Calcule o salário final do vendedor


import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


carros = int(input("Digite a quantidade de carros vendidos: "))
vendas = float(input("Digite o valor total de suas vendas: "))
salario_fixo = float(input("Digite o salário fixo: "))
comissao = float(input("Digite o valor por carro vendido: "))

salario = salario_fixo + (comissao * carros) + (vendas * 0.05)
#print("Salário final do vendedor: ", salario, "reais")

print(f' Salário final do vendedor: {salario:.2f}', "reais")
      
