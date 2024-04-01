import os  # o comando import possibilita a importação de pacotes, módulos e bibliotecas
os.system("cls") #para limpar a tela a cada iteração

# Solicita o número de horas trabalhadas no mês e o salário por hora
horas_trabalhadas_mes = float(input("Digite o número de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o salário por hora: "))

# Define a jornada de trabalho semanal e o número de semanas em um mês
horas_semanais = 40
semanas_por_mes = 4

# Calcula o total de horas regulares e extras trabalhadas no mês
horas_regulares = min(horas_trabalhadas_mes, horas_semanais * semanas_por_mes)
horas_extras = max(horas_trabalhadas_mes - horas_semanais * semanas_por_mes, 0)

# Calcula o salário total, incluindo horas extras, se houver
salario_total = (horas_regulares * salario_por_hora) + (horas_extras * salario_por_hora * 1.5)

# Exibe o salário total do funcionário
print(f"O salário total do funcionário é: R$ {salario_total:.2f}")