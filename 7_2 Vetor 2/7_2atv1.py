from biblioteca import *
import math

def calculaLucros (coxinha, quibe, lucro_coxinha, lucro_quibe):
    lucro = []
    for x in range(len(coxinha)):
        conta = coxinha[x] * lucro_coxinha + quibe[x] * lucro_quibe
        conta = round(conta,2)
        lucro.append(conta)
    return(lucro)

    
coxinha = inputVetor('Vendas de coxinhas: ', int)
quibe = inputVetor('Vendas de quibes: ', int)

if len(coxinha) != len(quibe):
    print('Dados de vendas inválidos')
else:
    lucro_coxinha = float(input('Lucro por unidade de coxinha: R$ '))
    lucro_quibe = float(input('Lucro por unidade de quibe: R$ '))
    
    lucro = calculaLucros(coxinha, quibe, lucro_coxinha, lucro_quibe)
    
    print(f'Lucros: {lucro}')
    
    maior = -math.inf
    menor = math.inf
    
    for x in range(len(lucro)):
        if lucro[x] > maior:
            maior = lucro[x]
        elif lucro[x] < menor:
            menor = lucro[x]
    
    print(f'Maior lucro = R$ {maior:.2f}')
    print(f'Menor lucro = R$ {menor:.2f}')