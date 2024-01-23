''' Programa para receber uma hora no formato de três números inteiros que representam
horas, minutos e segundos. O programa deve calcular e retornar a quantidade
total de segundos '''


import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


#dias = int(input("Digite a quantiadade de dias: "))
horas = int(input("Digite a quantiade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos
total_em_segundos = (horas * 3600) + (minutos * 60) + segundos
#total_em_segundos = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + segundos
print("A quantidade de segundos dos valores informados é:" ,total_em_segundos)