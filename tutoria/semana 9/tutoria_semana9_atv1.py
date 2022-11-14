vetor = []
print('Exercício 1')
print('-'*11)

dim_vetor = int(input('Qual a dimensão do vetor ? '))
print('Leitura dos elementos do vetor...')

for i in range(0, dim_vetor, 1):
    vetor.append(float(input(f'Elemento[{i}]: ')))
    
print('Resultados:')
#print(vetor)
n = len(vetor)
print('[', end='')
for i in range(n):
    print(f'{vetor[i]:6}', end='')
print('   ]')

soma = 0
multi = 1
for j in range(0, n, 1):
    soma += vetor[j]
    multi *= vetor[j]
    media_arit = soma/n
    media_geomet = multi**(1/n)

print(f'Média Aritmética: {media_arit:.4f}')
print(f'Média Geométrica: {media_geomet:.4f}')