''' Programa para ler a idade de uma pessoa expressa em ano, meses e dias e
escrever a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias
e mês com 30 dias '''

# variáveis utilizadas - anos, meses, dias, idade

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

anos = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite quantos meses tem do mês do seu nascimento até chegar dezembro: "))
dias = int(input("Digite quantos dias faltam do dia do seu nascimento para chegar no dia 30 do mês: "))
idade = (anos * 365) + (meses * 30) + dias 
print("A sua idade em dias é: ", idade)


# variáveis utilizadas - anos, mes, qtde_meses, dias, qtde_dias, idade

# anos = int(input("Digite quantos anos você tem: "))
# mes = int(input("Digite o número correspondente ao mês do seu nascimento: "))
# qtde_meses = int(12 - mes)
# dias = int(input("Digite o dia do seu nascimento: "))
# qtde_dias = int(30 - dias)
# idade = (anos * 365) + (qtde_meses * 30) + qtde_dias 
# print("A sua idade em dias é: ", idade)
