import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração


class EstadoBrasileiro:
    def __init__(self, nome_estado, num_municipios, populacao):
        self.nome_estado = nome_estado
        self.num_municipios = num_municipios
        self.populacao = populacao

    def exibir_informacoes(self):
        print("Nome do estado:", self.nome_estado)
        print("Número de municípios:", self.num_municipios)
        print("População:", self.populacao)


# Criando objetos para a classe EstadoBrasileiro
estado1 = EstadoBrasileiro("São Paulo", 645, 46289333)
estado2 = EstadoBrasileiro("Rio de Janeiro", 92, 17366189)
estado3 = EstadoBrasileiro("Minas Gerais", 853, 21292666)

# Exibindo informações dos estados
print("Informações dos estados:")
estado1.exibir_informacoes()
print("------------------------")
estado2.exibir_informacoes()
print("------------------------")
estado3.exibir_informacoes()