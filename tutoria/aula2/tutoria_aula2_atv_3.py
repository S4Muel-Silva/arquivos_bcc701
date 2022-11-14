valor = float(input('Qual o Valor Total da Compra? '))

if valor < 0:
    print('ERRO: Valor de compra inválida!')
    quit()
else:
    if 0 < valor <= 300:
        desconto = valor*0.02
    elif valor > 300 and valor <= 600:
        desconto = valor*0.04
    elif 600 < valor <= 900:
        desconto = valor*0.06
    else:
        desconto = valor*0.08

valor_desconto = valor - desconto

print(f'Valor do pagamento: R${valor_desconto:.2f}')