# 10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperatura_celsius = float(input('Qual a temperatura atual (ºC)?'))

def calcular_farenheit(valor):
    farenheit = (valor * 9/5) + 32
    return int(farenheit)

print('O valor da temperatura é ' + str(calcular_farenheit(temperatura_celsius)) + 'ºC')