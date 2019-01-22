# 13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input('Informe sua altura(m):'))
sexo_informado = input('Informe seu sexo(M/F):')

def calcular_peso_ideal(valor, sexo):
    if sexo == 'M':
        peso_ideal = (72.7 * valor) - 58
        return int(peso_ideal)
    elif sexo == 'F':
        peso_ideal = (62.1 * valor) - 44.7
        return int(peso_ideal)

print('Seu peso ideal é', str(calcular_peso_ideal(altura, sexo_informado)), 'kg')