print('Exercício 1 - Valor do Polinômio')
print()
grau = int(input('Qual o grau do polinômio ? '))

print('Leitura dos coeficientes do polinômio...')

vetor = []
soma = 0
for x in range(grau+1):
    elemento = float(input(f'Elemento na posição {x}: '))
    vetor.append(elemento)
x = float(input('Qual o valor de x ? '))

for y in range(grau, -1, -1):
    soma += vetor[y]*(x**y)

print(f'Valor de P({x}): {soma:.8f}')