''' Programa para fazer a conversão cambial entre reais e dólares.
Considere como taxa de câmbio US$ 1,00 = R$ 5,05. Leia um valor em
reais pelo teclado e mostre o correspondente em dólares '''


import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


#dias = int(input("Digite a quantiadade de dias: "))
valor_real = float(input("Digite o valor em reais a ser convertido: "))
valor_dolar = valor_real / 5.3
print("O valor em dólar é: " ,valor_dolar)
#print("O valor em dólar é: " ,round(valor_dolar, 2))