import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Lista para armazenar as temperaturas médias de cada mês
temperaturas = []

# Dicionário para associar os meses aos seus respectivos índices
meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto", 
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

# Loop para receber as temperaturas
for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média de {meses[mes]}: "))
    temperaturas.append(temperatura)

# Calculando a média anual das temperaturas
media_anual = sum(temperaturas) / len(temperaturas)

# Mostrando a média anual
print("Média anual das temperaturas:", media_anual)

# Mostrando as temperaturas acima da média anual e em que mês ocorreram
print("Temperaturas acima da média anual e os meses correspondentes:")
for mes, temperatura in enumerate(temperaturas, start=1):
    if temperatura > media_anual:
        print(f"{meses[mes]}: {temperatura}°C")