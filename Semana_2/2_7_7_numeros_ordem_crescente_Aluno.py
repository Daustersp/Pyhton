import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#ORDEM DECRESCENTE
#ORDEM CRESCENTE
primeiro = int(input('Digite o primeiro número: '))
segundo  = int(input('Digite o segundo número : '))
print(primeiro,'-',segundo)

if(primeiro > segundo):
    print(segundo,"-",primeiro)
else:
    print(primeiro,"-",segundo)