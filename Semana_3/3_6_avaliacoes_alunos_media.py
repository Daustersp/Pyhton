import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print('Aluno(a), foi aprovado(a)!')
else:
    print('Aluno(a), está reprovado(a)!')

print("A média foi:", media)