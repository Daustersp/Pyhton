#3. Fazer um sistema de Feira Livre(Deve imprimir 
# uma lista com as frutas e pedir para o solicitante 
# colocar o nome e selecionar a fruta e depois deve 
# imprimir o nome do solicitante e a fruta)-Criar 
# usando classes 

# from feira_class import feira_class

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class feira_class:
    def __init__ (self, nome_fruta):
        self.nome_fruta = nome_fruta


fruta_0 = feira_class("laranja")
fruta_1 = feira_class("maçã")
fruta_2 = feira_class("pêra")
fruta_3 = feira_class("uva")

print(f"Nossa Feira Livre tem disponível hoje:" #imprime as opções para o usuário
''' [0] laranja , [1] maçã , [2] pêra, [3] uva''')  
solicitante = str(input("Digite seu nome para comprar: "))   #solicita nome do usuário
selecao = int(input("Digite o número da fruta que deseja adquirir? "))   #solicita a seleção do usuáiro
lista_frutas = [fruta_0,fruta_1,fruta_2,fruta_3]    #lista de frutas
opcao_selecionada = int(selecao)
for opcao in lista_frutas:
        if opcao_selecionada <= 3:   #verifica a seleção
                print(f"{solicitante} agradecemos por adquirir a fruta {lista_frutas[opcao_selecionada].nome_fruta}.") #resultado
                print("Volte sempre!")
                break
        if opcao_selecionada >= 4:
                print(f"{solicitante} não temos essa fruta.")   #caso usuário digite opção inválida
                break