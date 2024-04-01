import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#SEM USAR FUNÇÃO
# Loop para ler e verificar a primeira nota
while True:
    nota1 = float(input("Digite a nota da 1ª avaliação: "))
    if 0 <= nota1 <= 10:
        break
    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

# Loop para ler e verificar a segunda nota
while True:
    nota2 = float(input("Digite a nota da 2ª avaliação: "))
    if 0 <= nota2 <= 10:
        break
    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Imprime a média das notas
print(f"A média das notas é: {media}")



# USANDO FUNÇÃO
# Função para verificar se uma nota é válida (entre 0 e 10)
# def nota_valida(nota):
#     return 0 <= nota <= 10

# Loop para ler e verificar a primeira nota
# while True:
#     nota1 = float(input("Digite a nota da 1ª avaliação: "))
#     if nota_valida(nota1):
#         break
#     print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

# Loop para ler e verificar a segunda nota
# while True:
#     nota2 = float(input("Digite a nota da 2ª avaliação: "))
#     if nota_valida(nota2):
#         break
#     print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")

# Calcula a média das notas
# media = (nota1 + nota2) / 2

# Imprime a média das notas
# print(f"A média das notas é: {media}")