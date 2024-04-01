import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Define o código de usuário e a senha correta
codigo_usuario_correto = 1234
senha_correta = 9999

# Solicita ao usuário que insira o código de usuário
codigo_usuario = int(input("Digite o código de usuário: "))

# Verifica se o código de usuário é válido
if codigo_usuario != codigo_usuario_correto:
    print("Usuário inválido!")
else:
    # Se o código de usuário for válido, solicita a senha
    senha = int(input("Digite a senha: "))
    
    # Verifica se a senha está correta
    if senha != senha_correta:
        print("Senha incorreta")
    else:
        print("Acesso permitido")