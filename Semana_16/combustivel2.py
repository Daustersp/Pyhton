import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor):
        """Abastece o veículo com combustível pelo valor especificado e mostra a quantidade de litros fornecida."""
        if valor <= 0:
            return "O valor deve ser positivo."
        
        litros_abastecidos = valor / self.valor_litro
        
        if litros_abastecidos > self.quantidade_combustivel:
            return f"Quantidade insuficiente de combustível. Só há {self.quantidade_combustivel:.2f} litros disponíveis."
        
        self.quantidade_combustivel -= litros_abastecidos
        return f"Abastecido com {litros_abastecidos:.2f} litros. Quantidade restante: {self.quantidade_combustivel:.2f} litros."

    def abastecerPorLitro(self, litros):
        """Abastece o veículo com a quantidade de litros especificada e mostra o valor a ser pago."""
        if litros <= 0:
            return "A quantidade de litros deve ser positiva."
        
        if litros > self.quantidade_combustivel:
            return f"Quantidade insuficiente de combustível. Só há {self.quantidade_combustivel:.2f} litros disponíveis."
        
        valor_a_pagar = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        return f"O valor a ser pago é R$ {valor_a_pagar:.2f}. Quantidade restante: {self.quantidade_combustivel:.2f} litros."

    def alterarValor(self, novo_valor):
        """Altera o valor do litro do combustível."""
        if novo_valor <= 0:
            return "O valor do litro deve ser positivo."
        self.valor_litro = novo_valor
        return f"Novo valor do litro: R$ {self.valor_litro:.2f}."

    def alterarCombustivel(self, novo_tipo):
        """Altera o tipo de combustível."""
        self.tipo_combustivel = novo_tipo
        return f"Novo tipo de combustível: {self.tipo_combustivel}."

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        """Altera a quantidade de combustível restante na bomba."""
        if nova_quantidade < 0:
            return "A quantidade de combustível não pode ser negativa."
        self.quantidade_combustivel = nova_quantidade
        return f"Nova quantidade de combustível: {self.quantidade_combustivel:.2f} litros."


# Solicitar os dados iniciais ao usuário
tipo_combustivel = input("Digite o tipo de combustível: ")
valor_litro = float(input("Digite o valor do litro do combustível (R$): "))
quantidade_combustivel = float(input("Digite a quantidade inicial de combustível (em litros): "))
    
# Criar uma instância da classe BombaCombustivel
bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)
    
while True:
    print("\nEscolha uma opção:")
    print("1. Abastecer por valor")
    print("2. Abastecer por litro")
    print("3. Alterar valor do litro")
    print("4. Alterar tipo de combustível")
    print("5. Alterar quantidade de combustível")
    print("6. Sair")
        
    opcao = int(input("Digite o número da opção desejada: "))
        
    if opcao == 1:
        valor = float(input("Digite o valor a ser abastecido (R$): "))
        print(bomba.abastecerPorValor(valor))
        
    elif opcao == 2:
        litros = float(input("Digite a quantidade de litros a ser abastecida: "))
        print(bomba.abastecerPorLitro(litros))
        
    elif opcao == 3:
        novo_valor = float(input("Digite o novo valor do litro (R$): "))
        print(bomba.alterarValor(novo_valor))
        
    elif opcao == 4:
        novo_tipo = input("Digite o novo tipo de combustível: ")
        print(bomba.alterarCombustivel(novo_tipo))
        
    elif opcao == 5:
        nova_quantidade = float(input("Digite a nova quantidade de combustível (em litros): "))
        print(bomba.alterarQuantidadeCombustivel(nova_quantidade))
        
    elif opcao == 6:
        print("Saindo...")
        break
        
    else:
        print("Opção inválida. Tente novamente.")