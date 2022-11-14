from biblioteca import*
import math
def calculosVetor(x):
    NumX=len(x); maior=-math.inf;menor=math.inf;soma=0
    for i in range(NumX):
        if x[i]>maior:
            maior=round(x[i],2)
        if x[i]<menor:
            menor=round(x[i],2)
        soma+=x[i]
    media=round(soma/NumX,2)
    return NumX,menor,maior,media
    
    
print("Manipulações de valores de Vetor")
x = inputVetor("Vetor X: ",float)

NumX,menor,maior,media = calculosVetor(x)

print("Propriedades do vetor X:")
print(f". Possui {NumX} elementos")
print(f". {menor:.2f} é o menor valor")
print(f". {maior:.2f} é o maior valor")
print(f". média dos valores é {media:.2f}")