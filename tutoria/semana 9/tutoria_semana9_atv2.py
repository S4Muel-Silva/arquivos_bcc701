vetor1 = []
vetor2 = []
vetor3 = []
print('Exercício 1')
print('-'*11)

dim = int(input('Qual a dimensão dos vetores ? '))

print('Leitura do primeiro vetor...')

for x in range(dim):
    vetor1.append(float(input(f'Elemento na posição [{x}]: ')))

print('Leitura do segundo vetor...')

for x in range(dim):
    vetor2.append(float(input(f'Elemento na posição [{x}]: ')))

for x in range(dim):
    vetor3.append((vetor1[x] + vetor2[x]) * 2)
 
print('Impressões dos resiltados:')
print('Vetor 1')
print('[', end='')
for x in range(dim):
    print(f' {vetor1[x]}  ', end='')
print(']')

print('Vetor 2')
print('[', end='')
for x in range(dim):
    print(f' {vetor2[x]}  ', end='')
print(']')

print('Vetor 3')
print('[', end='')
for x in range(dim):
    print(f' {vetor3[x]}   ', end='')
print(']')