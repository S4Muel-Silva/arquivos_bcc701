from biblioteca import*

M = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] , [ 7 , 8 , 9] , [ 10 , 11 , 12] ]

vetor = []

qtlin,qtcol = dimMatriz(M)

print('Exercício 3 - Análise das Linhas da Matriz')
print('------------------------------------------')
print('Resultados')
print('------------------------------------------')

print('Matriz:')
for lin in range(qtlin):
    print()
    for col in range(qtcol):
        print(f'{M[lin][col]:7}', end='')
print()
print()

for lin in range(qtlin):
    
    soma = 0
    prod = 1
    
    if lin == 0:
        for col in range(qtcol):
            
            soma += M[lin][col]
        vetor.append(soma)
    
    elif lin % 2 == 0:
        for col in range(qtcol):
            
            prod *= M[lin][col]
        vetor.append(prod)            
    
    else:
        for col in range(qtcol):
            
            soma += M[lin][col]
        vetor.append(soma)
       
print('Vetor Resultante: ')
print(vetor)