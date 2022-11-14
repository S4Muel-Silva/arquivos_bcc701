def calcDesconto (valor):
    if valor <= 250:
        desc = 0.03
        valordesc = valor*0.97
        
    elif 250 < valor <= 550:
        desc = 0.06
        valordesc = valor*0.94
        
    elif 550 < valor <= 750:
        desc = 0.08
        valordesc = valor*0.92
        
    else:
        desc = 0.1
        valordesc = valor*0.9
        
    return (desc, valordesc)

x = float(input('Defina o valor total da compra: R$ '))

if x <= 0:
    print('Erro: Valor total inválido.')
else:
    (res1, res2) = calcDesconto(x)
    print(f'Desconto de {res1*100:.0f}%.')
    print(f'Valor com desconto: R${res2:.2f}')