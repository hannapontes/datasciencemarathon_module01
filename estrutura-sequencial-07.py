# 07 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

largura = int(input('Informe a largura de um dos lados do quadrado:'))

def calcular_area_quadrado(valor):
    area_quadrado = valor**2
    return area_quadrado

def dobro(numero):
    return numero * 2

print('O dobro da área do quadrado é ' + str(dobro(calcular_area_quadrado(largura))) + 'm²')