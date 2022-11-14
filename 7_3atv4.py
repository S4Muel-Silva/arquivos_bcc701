from biblioteca import *

identidade = 0

matriz = inputMatriz('Digite os elementos da matriz: ',int)

qtlin, qtcol = dimMatriz(matriz)

for lin in range(qtlin):
    for col in range(qtcol):
        
        if lin == col:
            if matriz[lin][col] == 1:
                identidade += 1
        elif lin < col:
            if matriz[lin][col] == 0:
                identidade += 1
        elif lin > col:
            if matriz[lin][col] == 0:
                identidade += 1

print()

if identidade == qtlin*qtcol:
    print('A matriz é identidade. ')
else:
    print('A matriz não é identidade. ')