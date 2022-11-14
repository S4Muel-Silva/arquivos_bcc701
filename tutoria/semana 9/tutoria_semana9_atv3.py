vetor1 = []
vetor2 = []

print('Leitura do vetor (elementos float) ...')

cont = 0
valor = 0
while valor >= 0:
    valor = float(input('Digite um valor -->  '))
    vetor1.append(valor)
    cont += 1
vetor1.pop(cont-1)
    
tamanho = len(vetor1)
soma = 0

for x in range(tamanho):
    soma += vetor1[x]
    
    vetor2.append(soma)
    
print('Impressão dos Vetores Resultantes:')

print('Vetor lido:')

print('[', end='')
for x in range(tamanho):
    print(f'  {vetor1[x]}  ', end='')
print(']')

print('Vetor soma acumulada')

print('[', end='')
for x in range(tamanho):
    print(f'  {vetor2[x]}  ', end='')
print(']')