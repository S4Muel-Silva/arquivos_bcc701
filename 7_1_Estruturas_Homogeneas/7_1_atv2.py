from biblioteca import *

def estatNotas(vetor):
    maior = -100000
    menor = 100000
    media = 0
    tamanho = len(vetor)
    
    for i in range(tamanho):
        nota = vetor[i]
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        media += nota
        
    media = media/tamanho
    
    maior = round(maior,1)
    menor = round(menor,1)
    media = round(media,1)
    
    return (maior, menor, media)

def acimaMedia (vetor, media):
    vetor_res = []
    tamanho = len(vetor)
    
    for i in range(tamanho):
        nota = vetor[i]
        if nota > media:
            vetor_res.append(i)
    
    return(vetor_res)

vetor = inputVetor('Notas: ', float)
(maior, menor, media) = estatNotas(vetor)

print(f'Maior nota: {maior:.1f}')
print(f'Menor nota: {menor:.1f}')
print(f'Nota média: {media:.1f}')

vetor_res = acimaMedia(vetor, media)

print('Notas acima da média:')

tamanho2 = len(vetor_res)

for i in range(tamanho2):
    nota = vetor[ vetor_res[i] ]
    print(f'  - [{vetor_res[i]}] = {nota:.1f}')