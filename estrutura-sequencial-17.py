''' 17
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
area_pintada = float(input('Qual o tamanho(m²) da área pintada?'))
cobertura = area_pintada/6
preco1 = 80.0
capacidade1 = 18
preco2 = 25.0
capacidade2 = 3.6

latas1 = cobertura/capacidade1
situacao1 = latas1 * preco1
latas2 = cobertura/capacidade2
situacao2 = latas2 * preco2

print('Se você for comprar apenas latas de 18L você usará', int(latas1), 'latas e gastará R$', int(situacao1))
print('Se você for comprar apenas latas de 3,6L você usará', int(latas2), 'latas e gastará R$', int(situacao2))