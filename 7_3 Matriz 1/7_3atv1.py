from biblioteca import*
import math

matriz = inputMatriz("Matriz de notas: ", float)

menor = math.inf
maior = -math.inf

qtlin, qtcol = dimMatriz(matriz)

for lin in range(qtlin):
    for col in range(qtcol):
        
        if matriz[lin][col] < menor:
            menor = matriz[lin][col]
            
        if matriz[lin][col] > maior:
            maior = matriz[lin][col]
            
vetorMenor = []
vetorMaior = []

for lin in range(qtlin):
    for col in range(qtcol):
        
        if matriz[lin][col] == menor:
            vetorMenor.append(lin)
            
        if matriz[lin][col] == maior:
            vetorMaior.append(lin)
            
print(f'Menor nota: {menor}')
print('Alunos com a menor nota:')

for x in range(len(vetorMenor)):
    print(f'. {vetorMenor[x]}')
    
print(f'Maior nota: {maior}')
print('Alunos com a maior nota:')

for x in range(len(vetorMaior)):
    print(f'. {vetorMaior[x]}')
    
        
        
        
        