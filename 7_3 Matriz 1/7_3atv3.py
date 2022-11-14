from biblioteca import *

matriz = inputMatriz('Digite os elementos da matriz: ', int)
print()
qtlin, qtcol = dimMatriz(matriz)

alt = int(input('Digite a coluna que será alterada: '))

while alt < 0 or alt > qtcol-1:
    alt = int(input('Digite uma coluna válida: '))

for lin in range(qtlin):
    for col in range(qtcol):
        
        if col == alt:
           matriz[lin][col] *= 2
           
print()
print('Matriz alterada:')
for lin in range(qtlin):
    if 0 < lin < qtlin:
        print('; ', end='')
    
    for col in range(qtcol):
        
        if col != qtcol-1:
            print(f'{matriz[lin][col]}', end=', ')
        else:
            print(f'{matriz[lin][col]}', end='')
            