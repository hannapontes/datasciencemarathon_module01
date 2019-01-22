while True:
    print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
    hora_trabalhada = float(input('Inserir o valor da hora trabalhada:'))
    qtd_horas = float(input('Inserir a quantidade de horas trabalhadas:'))
    custo_material = float(input('Inserir custos com material:'))
    lucro = float(input('Qual a margem de lucro que deseja receber com a peça (%)?'))
    print('/-/-/-/-/-/-/-/-/-/-/-/-/-/-/')
    def calcular_valor_peca(valor, horas, material, lucro):
        mao_de_obra = valor*horas
        preco_unitario = mao_de_obra + material
        calculo_lucro = preco_unitario * (lucro/100)
        preco_venda = preco_unitario + calculo_lucro
        return preco_venda

    print('Sua peça deve custar no mínimo', str(calcular_valor_peca(hora_trabalhada, qtd_horas, custo_material, lucro)), 'reais')