import math
def calculaComprimento(r):
    c = math.sqrt((r["B"]["X"] - r["A"]["X"])**2 + (r["B"]["Y"] - r["A"]["Y"])**2)
    return round(c, 2)

retas = int(input('Informe a quantidade de retas: '))
vetor = []
for i in range(retas):
    print(f'Reta {i + 1}:')
    A = {}; B= {}; reta = {}
    A["X"] = float(input('- Coordenada X de A: '))
    A["Y"]= float(input('- Coordenada Y de A: '))
    B["X"]= float(input('- Coordenada X de B: '))
    B["Y"]= float(input('- Coordenada Y de B: '))
    reta["A"]= A
    reta["B"] = B
    qtd = calculaComprimento(reta)
    
    vetor.append(qtd)
    
print('Medidas das retas:')
for x in range(len(vetor)):
    print(f'Reta {x + 1}: {vetor[x]:.2f}')
    