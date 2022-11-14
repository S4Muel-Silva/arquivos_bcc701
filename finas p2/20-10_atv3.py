from biblioteca import *

print("Ministério do Meio Ambiente")
Meta = inputVetor("Metas dos estados: ", int)
Plant = inputMatriz("Plantio de árvores: ", int)
soma = 0

for col in range(len(Plant[0])):
    for lin in range(len(Plant)):
        soma += Plant[lin][col]
    if soma < Meta[col]:
        print(f"Estado {col+1}, meta = {Meta[col]}, plantio = {soma}")
    soma = 0