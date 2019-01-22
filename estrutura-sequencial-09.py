# 09 Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
temperatura_farenheit = float(input('Qual a temperatura atual (F)?'))

def calcular_celsius(valor):
    celsius = (5 * (valor-32) / 9)
    return int(celsius)

print('O valor da temperatura é ' + str(calcular_celsius(temperatura_farenheit)) + 'ºC')