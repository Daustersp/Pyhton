import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Lista principal
lista_principal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Lista derivada do intervalo da posição 0 a 9
lista_intervalo1 = lista_principal[0:9]

# Lista derivada do intervalo da posição 7 a 13
lista_intervalo2 = lista_principal[7:13]

# Imprimindo as listas derivadas
print("Lista derivada do intervalo da posição 1 a 9:", lista_intervalo1)
print("Lista derivada do intervalo da posição 8 a 13:", lista_intervalo2)