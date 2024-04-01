import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira o nome dos times e o número de gols marcados
time1 = input("Digite o nome do primeiro time: ")
gols_time1 = int(input(f"Digite o número de gols marcados pelo {time1}: "))

time2 = input("Digite o nome do segundo time: ")
gols_time2 = int(input(f"Digite o número de gols marcados pelo {time2}: "))

# Determina o vencedor ou se houve empate
if gols_time1 > gols_time2:
    vencedor = time1
elif gols_time2 > gols_time1:
    vencedor = time2
else:
    vencedor = "EMPATE"

# Exibe o nome do vencedor ou "EMPATE"
print(f"O vencedor da partida é: {vencedor}")