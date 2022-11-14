from biblioteca import*

def calculaConsumos(vetor_capacidade, matriz_km):
    qtlin, qtcol = dimMatriz(matriz_km)
    
    for lin in range(qtlin):
        for col in range(qtcol):
            calc = matriz_km[lin][col] / vetor_capacidade[col]
            calc = round(calc,2)
            
            matriz_km[lin][col] = calc
    matriz_res = matriz_km
    
    return(matriz_res)

def calculaMedias(matriz_res):
    qtlin, qtcol = dimMatriz(matriz_res)
    calc = 0
    vetor_res = []
    
    for lin in range(qtcol):
        calc = 0
        for col in range(qtlin):
            calc += matriz_res[col][lin]
        calc /= qtlin
        calc = round(calc,2)
        vetor_res.append(calc)
    return(vetor_res)
    
print('Teste de consumo')
vetor_capacidade = inputVetor('Capacidade dos tanques: \n>>> ', int)

if vetor_capacidade == []:
    print('É necessário pelo menos um automóvel')

else:
    matriz_km = inputMatriz('Quilometragens dos condutores: \n>>> ', int)
    
    qtlin, qtcol = dimMatriz(matriz_km)
    
    if matriz_km == [ ]:
        print('Deve haver pelo menos um condutor')
    
    elif qtcol != len(vetor_capacidade):
        print('Quantidade de automóveis incompatível')
    
    else:
        matriz_res = calculaConsumos(vetor_capacidade, matriz_km)
        
        print('Consumos km/l: ')
        
        for lin in range(qtlin):
            print(matriz_res[lin])
        
        vetor_res = calculaMedias(matriz_res)
        
        print('Médias dos consumos por automóvel: ')
        print(vetor_res)