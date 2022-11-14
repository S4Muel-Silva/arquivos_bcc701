from biblioteca import *

def contabilizarDemandas(idades):
    vetor = criarVetor(4, 0)
    
    for x in range(len(idades)):
        
        if idades[x] >= 85:
            vetor[0] += 1
        elif 85 > idades[x] >= 65:
            vetor[1] += 1
        elif 65 > idades[x] >= 45:
            vetor[2] += 1
        elif idades[x] >= 18:
            vetor[3] += 1
    
    return vetor

def avaliaAtendimento(vetor, vacinas):
    
    for x in range(len(vetor)):
        if vetor[x] <= vacinas[x]:
            res = True
        else:
            res = False
            
    return res

idades = inputVetor('Defina as idades dos habitantes: ', int)

vetor = contabilizarDemandas(idades)

print(f'Demandas a serem atendidas por faixa etária: ')

print(f'. >= 85.........: {vetor[0]}')
print(f'. < 85 e >= 65.: {vetor[1]}')
print(f'. < 65 e >= 45.: {vetor[2]}')
print(f'. >= 18.........: {vetor[3]}')

vacinas = inputVetor('Defina as disponibilidades de vacinas: ', int)

res = avaliaAtendimento(vetor, vacinas)

if res == True:
    print('A quantidade de vacinas é suficiente.')
else:
    print('Infelizmente, precisaremos de mais vacinas.')