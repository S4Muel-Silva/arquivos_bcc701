from biblioteca import *
def comparaVetores(vetor1, vetor2):
    vetor3 = []
    
    for x in range(len(vetor1)):
        subt = vetor1[x] - vetor2[x]
        
        if subt == 0:
            vetor3.append('E')
        elif subt < 0:
            vetor3.append('A')
        else:
            vetor3.append('R')
    return(vetor3)
    
def classificaEstado(vetor3):
    A = 0
    R = 0
    E = 0
    for x in range(len(vetor3)):
        
        if vetor3[x] == 'A':
            A += 1
        elif vetor3[x] == 'R':
            R += 1
        elif vetor3[x] == 'E':
            E += 1
    
    if A > R:
        res = 'Onda Vermelha'
    elif R > A:
        res = 'Onda Verde'
    else:
        res = 'Onda Amarela'
    
    return res
    
vetor1 = inputVetor('Número de mortes na semana anterior: ', int)
vetor2 = inputVetor('Número de mortes na semana atual: ', int)

if len(vetor1) != len(vetor2):
    print(f'Número de elementos incompatível ({len(vetor1)} != {len(vetor2)})')
else:
    vetor3 = comparaVetores(vetor1, vetor2)
    print('Classificações das macro-regiões:')
    print(vetor3)
    
    classif = classificaEstado(vetor3)
    
    print(f'Classificação do estado: {classif}')
    
    