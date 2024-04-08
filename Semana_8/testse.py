import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Recebe a lista
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Gera a lista derivada do intervalo de 1 a 9
lista_derivada = [x for x in lista_original if 1 <= x <= 9]

# Imprime a lista derivada
print(lista_derivada)