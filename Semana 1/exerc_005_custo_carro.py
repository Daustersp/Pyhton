''' Programa para ler o custo de fábrica de um carro, calcular e escrever
o curso final ao consumidor '''


import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


custo_fab = float(input("Digite o custo da fábrica de um carro: "))
imposto = custo_fab * (45 / 100)
dist = custo_fab * (28 / 100)
custo_total = custo_fab + imposto + dist
#print("O custo final para o consumidor será de: ", custo_total, "reais")

print(f' O custo final para o consumidor será de: {custo_total:.2f}', "reais")
      
