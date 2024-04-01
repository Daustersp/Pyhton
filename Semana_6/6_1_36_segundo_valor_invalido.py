import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

while True:
    # Solicita ao usuário que insira os dois valores
    valor1 = float(input("Digite o primeiro valor: "))
    
    # Verifica se o primeiro valor é zero
    if valor1 == 0:
        print("VALOR INVÁLIDO. O primeiro valor não pode ser zero.")
    else:
        valor2 = float(input("Digite o segundo valor: "))
        
        # Verifica se o segundo valor é zero
        if valor2 == 0:
            print("VALOR INVÁLIDO. O segundo valor não pode ser zero.")
        else:
            # Calcula e imprime o resultado da divisão
            resultado = valor1 / valor2
            print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado}")
            break