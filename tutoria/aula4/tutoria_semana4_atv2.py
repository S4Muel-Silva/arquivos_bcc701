def Calculos (a, b):
    valor_100kW = 1 / 7 * a
    valor_k = valor_100kW / 100
    
    valor_total = valor_k * b
    
    valor_desconto = valor_total * 0.1
    valor_desconto = valor_total - valor_desconto
    
    return (valor_k, valor_total, valor_desconto)

print('Cálculo do Custo da Energia Elértica')

salario = float(input('Informe o valor do Salário Mínimo (R$): '))
consumo = float(input('Informe a quantidade gasta de quilowatts (kW): '))

a, b, c = Calculos(salario, consumo)

print(f'Valor de cada quilowatt (R$): {a:.2f}')
print(f'Custo da energia elética sem o desconto (R$): {b:.2f}')
print(f'Custo da enegia elétrica (desconto de 10%) (R$): {c:.2f}')
