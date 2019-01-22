# 06 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
raio = int(input('Inserir raio do cículo:'))

def calcular_area(valor):
    area = 3.14 * (raio**2)
    return area

print('A área do círculo é ' + str(calcular_area(raio)) + 'm²')