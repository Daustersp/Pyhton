import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita o usuário a digitar o ano
ano = int(input("Digite um ano para verificar se é bissexto: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")