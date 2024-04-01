import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita a hora de início e a hora de fim do jogo de xadrez
hora_inicio = int(input("Digite a hora de início do jogo (inteiro): "))
hora_fim = int(input("Digite a hora de fim do jogo (inteiro): "))

# Calcula a duração do jogo
if hora_inicio <= hora_fim:
    duracao = hora_fim - hora_inicio
else:
    # Se o jogo começar em um dia e terminar no dia seguinte
    duracao = 24 - hora_inicio + hora_fim

# Exibe a duração do jogo
print(f"A duração do jogo foi de {duracao} horas.")