import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira o número do empregado, o ano de nascimento e o ano de ingresso na empresa
codigo_empregado = int(input("Digite o número do empregado (código): "))
ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
ano_ingresso = int(input("Digite o ano de ingresso na empresa: "))

# Calcula a idade do empregado
idade = 2024 - ano_nascimento

# Calcula o tempo de trabalho do empregado
tempo_trabalho = 2024 - ano_ingresso

# Verifica se o empregado está qualificado para a aposentadoria
if idade >= 65 or tempo_trabalho >= 30 or (idade >= 60 and tempo_trabalho >= 25):
    mensagem = "Requerer aposentadoria"
else:
    mensagem = "Não requerer"

# Exibe as informações e a mensagem
print(f"Empregado {codigo_empregado}:")
print(f"Idade: {idade} anos")
print(f"Tempo de trabalho: {tempo_trabalho} anos")
print(mensagem)