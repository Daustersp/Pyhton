import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

salario_atual = float(input("Digite o salário atual do empregado: R$ "))
percentual_aumento = float(input("Digite o percentual de aumento (em %): "))

aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + aumento

print("\nValor do aumento: R$", aumento)
print("Novo salário: R$", novo_salario)