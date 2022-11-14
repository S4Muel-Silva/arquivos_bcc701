import math
q = int(input('Digite a quantidade de lados: '))

if q < 3:
    print('Não é um polígono')
    quit()
if q > 6:
    print('Polígono não identificado')
    quit()
else:
    L = float(input('Digite a medida do lado: '))
    if q == 3:
        tipo = 'triângulo'
        area = (L**2)*(3**(1/2)) / 4
    elif q == 4:
        tipo = 'quadrado'
        area = L**2
    elif q == 5:
        tipo = 'pentágono'
        area = 5*(L**2) / (4*math.tan(0.6283))
    else:
        tipo = 'hexágono'
        area = 3*(L**2)*(3**(1/2)) / 2
print(f'O polígono é um {tipo} com área: {area:.2f}')