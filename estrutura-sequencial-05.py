#05 Faça um Programa que converta metros para centímetros.
metros = int(input('Informe quantos metros deseja converter:'))

def converter_centimetros(valor):
    conversao = valor * 100
    return conversao

print('O equivalente a '+ str(metros) + 'm é ' + str(converter_centimetros(metros)) + 'cm')