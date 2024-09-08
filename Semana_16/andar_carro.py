import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class Carro:
    def __init__(self, consumo_km_por_litro):
        """
        Inicializa um carro com o consumo de combustível especificado e o nível de combustível inicial como 0.
        
        :param consumo_km_por_litro: Consumo do carro em km por litro
        """
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_gasolina = 0

    def adicionarGasolina(self, litros):
        """
        Adiciona gasolina ao tanque do carro.
        
        :param litros: Quantidade de gasolina a ser adicionada
        :return: Mensagem confirmando a adição de gasolina
        """
        if litros > 0:
            self.nivel_gasolina += litros
            return f"Adicionado {litros:.2f} litros. Nível atual de gasolina: {self.nivel_gasolina:.2f} litros."
        else:
            return "A quantidade de gasolina a ser adicionada deve ser positiva."

    def andar(self, distancia):
        """
        Simula o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível.
        
        :param distancia: Distância a ser percorrida em km
        :return: Mensagem indicando a distância percorrida e o nível de gasolina restante
        """
        if distancia <= 0:
            return "A distância deve ser positiva."
        
        gasolina_necessaria = distancia / self.consumo_km_por_litro
        
        if gasolina_necessaria > self.nivel_gasolina:
            return f"Combustível insuficiente para andar {distancia} km. Só há {self.nivel_gasolina:.2f} litros disponíveis."
        
        self.nivel_gasolina -= gasolina_necessaria
        return f"Anda {distancia} km. Nível de gasolina restante: {self.nivel_gasolina:.2f} litros."

    def obterGasolina(self):
        """
        Retorna o nível atual de combustível no tanque.
        
        :return: Mensagem com o nível atual de gasolina
        """
        return f"Nível atual de gasolina: {self.nivel_gasolina:.2f} litros."

print("Bem-vindo ao simulador de carro!")
    
# Solicitar o consumo de combustível ao usuário
consumo = float(input("Digite o consumo de combustível do carro (km/litro): "))
    
# Criar uma instância da classe Carro
meuCarro = Carro(consumo)
    
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar gasolina")
    print("2. Andar")
    print("3. Obter nível de gasolina")
    print("4. Sair")
        
    opcao = int(input("Digite o número da opção desejada: "))
        
    if opcao == 1:
        litros = float(input("Digite a quantidade de gasolina a ser adicionada (litros): "))
        print(meuCarro.adicionarGasolina(litros))
        
    elif opcao == 2:
        distancia = float(input("Digite a distância a ser percorrida (km): "))
        print(meuCarro.andar(distancia))
        
    elif opcao == 3:
        print(meuCarro.obterGasolina())
        
    elif opcao == 4:
        print("Saindo...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")