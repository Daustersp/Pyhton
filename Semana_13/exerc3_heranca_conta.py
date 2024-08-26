# Herança

import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

class ContaCorrente:
    def __init__(self, numero_conta, saldo):
        self.numero_conta = numero_conta
        self.saldo = saldo

    def creditar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Crédito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Valor para crédito deve ser positivo.")

    def debitar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Débito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente para débito.")
        else:
            print("Valor para débito deve ser positivo.")

class Poupanca(ContaCorrente):
    def __init__(self, numero_conta, saldo, taxa_juros):
        super().__init__(numero_conta, saldo)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        if self.taxa_juros > 0:
            juros = self.saldo * (self.taxa_juros / 100)
            self.saldo += juros
            print(f"Juros de R$ {juros:.2f} aplicados. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Taxa de juros deve ser positiva.")

class ContaImposto(ContaCorrente):
    def __init__(self, numero_conta, saldo, percentual_imposto):
        super().__init__(numero_conta, saldo)
        self.percentual_imposto = percentual_imposto

    def calcula_imposto(self):
        if self.percentual_imposto > 0:
            imposto = self.saldo * (self.percentual_imposto / 100)
            self.saldo -= imposto
            print(f"Imposto de R$ {imposto:.2f} calculado e subtraído. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Percentual de imposto deve ser positivo.")

# Código de teste

# Criar uma conta corrente
conta_corrente = ContaCorrente(numero_conta="12345", saldo=1000.00)
print("Conta Corrente:")
conta_corrente.creditar(200.00)
conta_corrente.debitar(150.00)
print(f"Número da conta: {conta_corrente.numero_conta}")
print(f"Saldo atual: R$ {conta_corrente.saldo:.2f}")

# Criar uma conta poupança
conta_poupanca = Poupanca(numero_conta="67890", saldo=1500.00, taxa_juros=2.5)
print("\nConta Poupança:")
conta_poupanca.aplicar_juros()
print(f"Número da conta: {conta_poupanca.numero_conta}")
print(f"Saldo atual: R$ {conta_poupanca.saldo:.2f}")
print(f"Taxa de juros: {conta_poupanca.taxa_juros}%")

# Criar uma conta com imposto
conta_imposto = ContaImposto(numero_conta="54321", saldo=2000.00, percentual_imposto=1.0)
print("\nConta com Imposto:")
conta_imposto.calcula_imposto()
print(f"Número da conta: {conta_imposto.numero_conta}")
print(f"Saldo atual: R$ {conta_imposto.saldo:.2f}")
print(f"Percentual de imposto: {conta_imposto.percentual_imposto}%")