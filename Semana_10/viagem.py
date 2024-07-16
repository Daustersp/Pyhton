import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

#1. Fazer um cadastro de viagem (Deve pedir o nome do 
# viajante, dar as opções de destino e imprimir a 
# selecionada)-Criar usando classes

# from viagem_class import viagem_class # Caso em tenha um arquivo separado para as Classes

class Viagem:
    def __init__(self, destino):
        self.destino = destino

viagem_0 = Viagem("Bonito/MS")
viagem_1 = Viagem("Foz do Iguaçu/PR")
viagem_2 = Viagem("Santa Catarina/SC")
viagem_3 = Viagem("Belo Horizonte/MG")
viagem_4 = Viagem("Pantanal/MT")

print("Bem-vindo! Viagens IFB tem algumas ofertas para você!")
viajante = input("Digite seu nome para começarmos: ")
print(f"{viajante} temos 5 destinos que combinam com você:"
'''
[0] Bonito/MS
[1] Foz do Iguaçu/PR
[2] Santa Catarina/SC
[3] Belo Horizonte/MG
[4] Pantanal/MT''')

opcao_selecionada = int(input("Selecione o número da viagem desejada: "))   #solicitação ao usuário
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3, viagem_4] #lista dos índices dos objetos para escolha
if opcao_selecionada >= 5:    #caso usuário não digite a opção correta
    print("Esta opção não está incluída em nossos destinos.")

if opcao_selecionada <= 4:     #verifica a seleção
    print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino} está marcada.") #resultado
    print("Volte sempre!")
