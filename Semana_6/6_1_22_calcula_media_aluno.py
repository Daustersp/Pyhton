import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita ao usuário que insira as notas e a média dos exercícios
N1 = float(input("Digite a nota da primeira verificação: "))
N2 = float(input("Digite a nota da segunda verificação: "))
N3 = float(input("Digite a nota da terceira verificação: "))
media_exercicios = float(input("Digite a média dos exercícios: "))

# Calcula a média de aproveitamento
media_aproveitamento = (N1 + N2 * 2 + N3 + media_exercicios) / 6

# Determina o conceito do aluno
if media_aproveitamento >= 9:
    conceito = "A"
elif media_aproveitamento >= 7.5:
    conceito = "B"
elif media_aproveitamento >= 6.0:
    conceito = "C"
else:
    conceito = "D"

# Exibe o conceito do aluno
print(f"O conceito do aluno é: {conceito}")