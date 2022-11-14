vmax = float(input('Velocidade máxima: '))
vmedida = float(input('velocidade medida: '))

if vmedida <= 0 or vmedida >= 300:
    print('Velocidade inválida')
else:
    v = vmedida - vmax
    
    if v <= 0:
        print('Motorista não cometeu infração')
    elif 0 < v <= 10:
        print('Multa de R$120.00 e 2 pontos na CNH')
    elif 10 < v <= 30:
        print('250.00 e 5')
    else:
        print('600.00 e 7')