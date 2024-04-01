import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita as idades dos homens
idade_homem1 = int(input("Digite a idade do primeiro homem: "))
idade_homem2 = int(input("Digite a idade do segundo homem: "))

# Solicita as idades das mulheres
idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
idade_mulher2 = int(input("Digite a idade da segunda mulher: "))

# Encontra o homem mais velho e a mulher mais nova
homem_mais_velho = max(idade_homem1, idade_homem2)
mulher_mais_nova = min(idade_mulher1, idade_mulher2)

# Encontra o homem mais novo e a mulher mais velha
homem_mais_novo = min(idade_homem1, idade_homem2)
mulher_mais_velha = max(idade_mulher1, idade_mulher2)

# Calcula a soma das idades do homem mais velho com a mulher mais nova
soma_idades = homem_mais_velho + mulher_mais_nova

# Calcula o produto das idades do homem mais novo com a mulher mais velha
produto_idades = homem_mais_novo * mulher_mais_velha

# Exibe os resultados
print(f"A soma das idades do homem mais velho com a mulher mais nova é: {soma_idades}")
print(f"O produto das idades do homem mais novo com a mulher mais velha é: {produto_idades}")