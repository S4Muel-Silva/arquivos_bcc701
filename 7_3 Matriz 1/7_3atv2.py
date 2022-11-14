from biblioteca import *

matriz = inputMatriz('Digite os elementos da matriz: ', int)

qtlin, qtcol = dimMatriz(matriz)

vetor = []

if qtlin != qtcol:
    print('A matriz não é quadrada.')
else:
    for lin in range(qtlin):
        for col in range(qtcol):
            
            if lin == col:
                vetor.append(matriz[lin][col])

    print('Elementos da diagonal principal:')
    
    for x in range(qtlin):
        if x != len(vetor)-1:
            print(f'{vetor[x]}', end=', ')
        else:
            print(f'{vetor[x]}')
                