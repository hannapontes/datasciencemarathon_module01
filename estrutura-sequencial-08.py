# 08 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

hora_trabalhada = float(input('Quanto você ganha por hora?'))
qtd_horas = float(input('Quantas horas foram trabalhas?'))

def calcular_salario(valor, horas):
    salario = horas*valor
    return salario

print('O valor a receber deve ser de', str(calcular_salario(hora_trabalhada, qtd_horas)), 'reais')
