# 04 Faça um Programa que peça as 4 notas bimestrais e mostre a média
lista_notas = []
for i in range(4):
    lista_notas.append(int(input('Informe a nota bimestral:')))

media = (lista_notas[0]+lista_notas[1]+lista_notas[2]+lista_notas[3])/len(lista_notas)
print('A média das notas é:', media)

