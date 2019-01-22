''' 15
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''

hora_trabalhada = float(input('Valor da hora trabalhada:'))
qtd_horas = float(input('Quantas horas foram trabalhadas no mês?'))

salario_bruto = hora_trabalhada * qtd_horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print('Salário Bruto: R$', salario_bruto)
print('Imposto de Renda(11%): R$', ir)
print('INSS(8%): R$', inss)
print('Sindicato(5%): R$', sindicato)
print('Salário Líquido: R$', salario_liquido)
