# 11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    o produto do dobro do primeiro com metade do segundo .
#    a soma do triplo do primeiro com o terceiro.
#    o terceiro elevado ao cubo.

inteiro01 = int(input('Inserir um numero inteiro:'))
inteiro02 = int(input('Inserir o segundo numero inteiro:'))
real = float(input('Inserir um numero real:'))

produto = (inteiro01*2)*(inteiro02/2)
soma = (inteiro01*3)+real
potencia = real**3

print('O produto do dobro do primeiro com metade do segundo:', produto)
print('A soma do triplo do primeiro com o terceiro:', soma)
print('O terceiro elevado ao cubo:', potencia)