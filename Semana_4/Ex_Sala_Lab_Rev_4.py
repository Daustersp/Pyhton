import os
os.system("cls")

# Usando posições na string
# email = "dauster.pereira@ifb.edu.br"
# print(email[0]) # mostra d
# print(email[1]) # mostra a
# print(email[2]) # mostra u
# print(email[3]) # mostra s
# print(email[4]) # mostra t
# print(email[5]) # mostra e
# print(email[6]) # mostra r
# print(email[7]) # mostra .
# print(email[0:6]) # mostra dauster
# print(len(email))


# Índice negativo
# email = "dauster.pereira@ifb.edu.br"
# print(email[-22]) # mostra t
# print(email[-1]) # mostra r
# print(email[-26]) # mostra d

# Usando o : antes da posição, mostra todos os dados até o caractere determinado (não incluso)
# email = "dauster.pereira@ifb.edu.br"
# print(email[:-21]) # mostra todos os dados até o caractere [-5] (não incluso)

# Usando o : depois da posição, mostra todos ao contrário com o caractere incluso (incluso)
# email = "dauster.pereira@ifb.edu.br"
# print(email[-5:]) # mostra todos os dados até o caractere [-5] (não incluso)

# Intervalo - [-126:-1] -> -16 (incluso) e -1 (não incluso)
# email = "dauster.pereira@ifb.edu.br"
# print(email[-26:-1]) # mostra todos os dados até o caractere [-5] (não incluso)


# Operações com string
# qtde_vendida = 1500
# custo_produto = 500
# lucro = qtde_vendida - custo_produto
# print ("O lucro da loja foi de " + lucro) #ERRO - só concatena string com string
# print ("O lucro da loja foi de " + str(lucro)) #Erro - só concatena string com string

#print ("O lucro da loja foi de: {}" .format(lucro))

# print ("O lucro da loja foi de: {} reais. O custo do produto foi de {} reais." .format(lucro, custo_produto))

# Uso do %s e %d
# qtde_vendida = 1500
# custo_produto = 500
# lucro = qtde_vendida - custo_produto
# print ("O lucro da loja foi de: %s " % "lucro")

# print ("O lucro da loja foi de: %d " % lucro)


# Uso do in
# print ("@" in "dauster.pereira@ifb.edu.br")

# print ("@" in "dauster.pereira.ifb.edu.br")

# Métodos para Str
# print(dir(str))

#Métodos importantes para Str
# texto = "dauster"
# print(texto.capitalize()) #Transforma a primeira letra em maiúscula

# texto = "DaUsTer"
# print(texto.casefold()) #Transforma a primeira letra em maiúscula

# texto = "dauster souza pereira"
# print(texto.count("a")) #Conta o número de vezes que um caractere aparece

# texto = "dauster souza pereira"
# print(texto.endswith("pereira")) #Verifica se a string termina com uma string específica

# texto = "dauster souza pereira"
# print(texto.find("p")) #Encontra a posição do termo procurado

# texto = "dauster123"
# print(texto.isalnum()) #Verifica se um texto é todo feito de caracteres alfanuméricos (letras e números)

# texto = "123"
# print(texto.isnumeric()) #Verifica seu um texto é todo feito por números

# texto = "1000.00"
# print(texto.replace(".", ",")) #Substitui um caractere escolhido por outro

# texto = "dauster.pereira@ifb.edu.br"
# print(texto.split("@")) #Separa o texto da STRING baseado em algum caractere indicado

# texto = "dauster souza pereira"
# print(texto.title()) #Coloca todas as letras iniciais das palavras MAIÚSCULAS

# texto = " H25P "
# print(texto.strip(" ")) #Retira os caracteres indesejados

# texto = "H25PEREIRA"
# print(texto.startswith("H25")) #Retorna TRUE se uma string se inicia com um texto específico

# texto = "jantei 3 vezes"
# print(texto.upper()) #Altera todo o texto para MAIÚSCULAS. Números ficam inalterados

# OUTRAS FORMATAÇÕES PERSONALIZADAS FORMAT
email = "dauster.pereira@ifb.edu.br"
print("Meu e-mail não é {}?".format(email)) #Formato padrão sem alinhamento

email = "dauster.pereira@ifb.edu.br"
print("Meu e-mail não é {:<30}?".format(email)) #Caixa de texto com tamanho de 30 caracteres e texto alinhado à esquerda (:<)

email = "dauster.pereira@ifb.edu.br"
print("Meu e-mail não é {:>30}?".format(email)) #Caixa de texto com tamanho de 30 caracteres e texto alinhado à direita (:>)

email = "dauster.pereira@ifb.edu.br"
print("Meu e-mail não é {:^30}?".format(email)) #Caixa de texto com tamanho de 30 caracteres e texto alinhado ao centro (:^)