''' 16
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
area_pintada = float(input('Qual o tamanho(m²) da área a ser pintada?'))
litros = area_pintada / 3
preco_por_lata = 80.0
capacidade_litros = 18

latas = litros / capacidade_litros
total = latas * preco_por_lata

print('Você usará', int(latas), 'para pintar a área desejada e gastará R$', int(total))