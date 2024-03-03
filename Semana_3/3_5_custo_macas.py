import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#ORDEM DECRESCENTE
qtde_macas = int(input('Digite a quantidade de maçãs compradas: '))

if (qtde_macas >= 12):
   custo_compra = qtde_macas * 1.00
else:
   custo_compra= qtde_macas * 1.30

print("O custo da compra foi de:", custo_compra, "reais")