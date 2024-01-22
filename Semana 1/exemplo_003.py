''' Programa para ler o número total de eleitores de um município, o número de votos brancos,
nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
de eleitores '''

# variáveis utilizadas - eleitores, votobranco, votonulo, percbranco, percnulo, percvalido

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

eleitores = int(input("Digite o total de eleitores do município: "))
votobranco = int(input("Digite a quantidade de votos brancos: "))
votonulo = int(input("Digite a quantidade de votos nulos: "))
percbranco = (votobranco * 100) / eleitores
percnulo = (votonulo * 100) / eleitores
percvalido = eleitores - (votobranco + votonulo) 
print("Votos brancos: ", percbranco, "%")
print("Votos nulos: ", percnulo, "%")
print("Votos válidos: ", (percvalido *100) / eleitores, "%")
