mo = float(input('Quantidade de Morangos (em kg): '))
ma = float(input('Quantidade de Maçãs (em kg): '))

if mo <0 or ma < 0:
    print('Entrada inválida')
else:   
    if mo <= 5:
        pre_mo = 2.5 * mo
    else:
        pre_mo = 2.2 * mo

    if ma <= 5:
        pre_ma = 1.8 * ma
    else:
        pre_ma = 1.5 * ma
    
    total = pre_mo + pre_ma
    print(f'O valor total da sua compra é R$ {total:.2f}')
