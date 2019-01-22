# 12 Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Informe sua altura:"))

def calcular_peso_ideal(valor):
    peso_ideal = (72.7*valor)-58
    return int(peso_ideal)

print('Seu peso ideal é', str(calcular_peso_ideal(altura)), 'kg')