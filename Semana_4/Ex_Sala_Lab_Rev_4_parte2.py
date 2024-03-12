import os
os.system("cls")

# OUTRAS FORMATAÇÕES PERSONALIZADAS FORMAT

# FORMATO PADRÃO SEM ALINHAMENTO
# email = "dauster.pereira@ifb.edu.br"
# print("Meu e-mail não é {}?".format(email))

''' CAIXA DE TEXTO COM TAMANHO DE 3O CARACTERES E 
TEXTO ALINHADO À ESQUERDA (:<)'''
# email = "dauster.pereira@ifb.edu.br"
# print("Meu e-mail não é {:<30}?".format(email))

'''CAIXA DE TEXTO COM TAMANHO DE 3O CARACTERES E 
TEXTO ALINHADO À DIREITA (:>)'''
# email = "dauster.pereira@ifb.edu.br"
# print("Meu e-mail não é {:>30}?".format(email)) 

'''CAIXA DE TEXTO COM TAMANHO DE 3O CARACTERES E 
TEXTO ALINHADO AO CENTRO (:^)'''
# email = "dauster.pereira@ifb.edu.br"
# print("Meu e-mail não é {:^30}?".format(email)) #Caixa de texto com tamanho de 30 caracteres e texto alinhado ao centro (:^)

'''CAIXA DE TEXTO COM TAMANHO DE 50 CARACTERES E 
TEXTO ALINHADO AO CENTRO (:^)'''
# email = "dauster.pereira@ifb.edu.br"
# print("Meu e-mail não é {:^50}?".format(email)) #Caixa de texto com tamanho de 30 caracteres e texto alinhado ao centro (:^)

# EDIÇÃO DE SINAL
# custo_produto = 800
# venda = 420
# lucro = venda - custo_produto
# print("A venda foi {:+} e o lucro foi {:+}" .format(venda, lucro))

# SEPARADOR DE MILHAR
# custo_produto = 8000
# venda = 4200
# lucro = venda - custo_produto
# print("A venda foi {:,} e o lucro foi {:,}" .format(venda, lucro))

# EDIÇÃO DE SINAL E SEPARADOR DE MILHAR
# custo_produto = 8000
# venda = 4200
# lucro = venda - custo_produto
# print("A venda foi {:+,} e o lucro foi {:+,}" .format(venda, lucro))

# CASAS DECIMAIS FIXAS - por padrão tem 6 casas decimais
# custo_produto = 8000
# venda = 4200
# lucro = venda - custo_produto
# print("A venda foi {:f} e o lucro foi {:f}" .format(venda, lucro))

# CASAS DECIMAIS FIXAS - especificando
# custo_produto = 8000
# venda = 4200
# lucro = venda - custo_produto
# print("A venda foi {:.2f} e o lucro foi {:.1f}" .format(venda, lucro))

# FORMATO PERCENTUAL - sem definir qtde de casas decimais
# custo_produto = 600
# venda = 1500
# lucro = venda - custo_produto
# margem = lucro / venda
# print("A margem de lucro foi de {:%}".format(margem))

# FORMATO PERCENTUAL - definindo qtde de casas decimais
# custo_produto = 600
# venda = 1500
# lucro = venda - custo_produto
# margem = lucro / venda
# print("A margem de lucro foi de {:.2%}".format(margem))

# FORMATO MOEDA - combinação de formatos
# custo_produto = 6000
# venda = 13000
# lucro = venda - custo_produto
# print("A venda foi de R$ {:,.2f} e a margem de lucro foi de R$ {:,.2f}".format(venda, lucro))

# FORMATO MOEDA - uso do underline
# custo_produto = 6000
# venda = 13000
# lucro = venda - custo_produto

# lucro_texto = "R${:_.2f}".format(lucro) #substituir o ponto do milhar por _
# print("O lucro é de ", lucro_texto.replace(".",",").replace("_",".")) #substituir . por , e _ por .

# FUNÇÃO ROUND
# imposto_de_renda = 0.15578
# preco = 100
# valor_imposto = round(preco - imposto_de_renda, 1)
# print("Imposto de renda sobre o preço é de {}".format(valor_imposto))
