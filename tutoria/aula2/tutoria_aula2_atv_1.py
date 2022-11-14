valor = float(input('INFORME O VALOR DA COMPRA: '))

if valor <= 150:
    desconto = valor*0.10
if valor > 150:
    desconto = valor*0.20

print(f'VALOR DO DESCONTO: R${desconto:.2f}')

valor_desconto = valor - desconto

imposto = valor_desconto*0.08

print(f'VALOR DA COMPRA COM O DESCONTO: R${valor_desconto:.2f}')

print(f'VALOR DO IMPOSTO: R${imposto:.2f}')

total = valor_desconto + imposto

print(f'TOTAL A PAGAR: R${total:.2f}')