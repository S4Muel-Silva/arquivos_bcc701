import math

print('Quantidade de ladrilhos\n-----------------------')

tipo = float(input('Qual o tipo de ladrilho (1/2/3)? '))

if tipo != 1 and tipo != 2 and tipo != 3:
    print(f'ERRO: o ladrilho tipo {tipo} é inválido')
    quit()
else:
    area = float(input('Qual a área (cm²) da sala? '))
    
    if tipo==1:
        quant = area/80
    elif tipo==2:
        quant = area/60
    else:
        quant = area/40

quant = math.ceil(quant)

print(f'Quantidade de ladrilhos: {quant}')
