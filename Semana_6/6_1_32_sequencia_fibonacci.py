import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Função para gerar a sequência de Fibonacci
def fibonacci(n):
    # Inicializa os primeiros dois termos da sequência
    fib = [0, 1]

    # Calcula os próximos termos da sequência até o número desejado
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib

# Solicita ao usuário que insira o número de termos desejado
N = int(input("Digite o número de termos da sequência de Fibonacci: "))

# Chama a função para gerar a sequência de Fibonacci com N termos
sequencia = fibonacci(N)

# Exibe a sequência de Fibonacci
print("Sequência de Fibonacci:")
for termo in sequencia:
    print(termo, end=" ")