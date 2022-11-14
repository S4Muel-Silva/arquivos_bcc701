import math

tipo = int(input('Tipo de ladrilho (1 ou 2): '))
area = float(input('Área da sala: '))

if tipo == 1:
    total = area / 80
if tipo == 2:
    total = area / 60
    
total = math.ceil(total)

print(f'Quantidade de ladrilhos: {total}')
