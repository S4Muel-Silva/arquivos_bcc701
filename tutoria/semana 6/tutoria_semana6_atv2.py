import math
cont = 5
aproveitados = 0
peso_total = 0
maior = -math.inf

for i in range(1, cont+1, 1):
    ml = float(input(f'Digite a massa do lingote {i}: '))
    
    if ml > 24.9:
        aproveitados += 1
        peso_total += ml
        
        if ml > maior:
            maior = ml

print(f'Número de lingotes aproveitados: {aproveitados}')

media = peso_total / aproveitados

print(f'Peso médio dos lingotes aproveitados: {media:.1f} kg')

print(f'Maior peso de um lingote aproveitado: {maior:.1f} kg')
