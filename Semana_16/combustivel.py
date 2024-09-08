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
            return f"Quantidade insuficiente de combustível. Só há {self.quantidade_combustivel} litros disponíveis."
        
        self.quantidade_combustivel -= litros_abastecidos
        return f"Abastecido com {litros_abastecidos:.2f} litros. Quantidade restante: {self.quantidade_combustivel:.2f} litros."

    def abastecerPorLitro(self, litros):
        """Abastece o veículo com a quantidade de litros especificada e mostra o valor a ser pago."""
        if litros <= 0:
            return "A quantidade de litros deve ser positiva."
        
        if litros > self.quantidade_combustivel:
            return f"Quantidade insuficiente de combustível. Só há {self.quantidade_combustivel} litros disponíveis."
        
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


# Criando uma instância da classe BombaCombustivel
bomba = BombaCombustivel(tipo_combustivel="Gasolina", valor_litro=5.50, quantidade_combustivel=1000)
    
# Exibindo informações iniciais
print(f"Tipo de combustível: {bomba.tipo_combustivel}")
print(f"Valor do litro: R$ {bomba.valor_litro:.2f}")
print(f"Quantidade de combustível: {bomba.quantidade_combustivel:.2f} litros")

# Abastecer por valor
print("\nAbastecimento por valor:")
print(bomba.abastecerPorValor(55))  # Abastecer com R$ 55

# Abastecer por litro
print("\nAbastecimento por litro:")
print(bomba.abastecerPorLitro(10))  # Abastecer com 10 litros

# Alterar valor do litro
print("\nAlterar valor do litro:")
print(bomba.alterarValor(6.00))

# Alterar tipo de combustível
print("\nAlterar tipo de combustível:")
print(bomba.alterarCombustivel("Álcool"))

# Alterar quantidade de combustível
print("\nAlterar quantidade de combustível:")
print(bomba.alterarQuantidadeCombustivel(1200))