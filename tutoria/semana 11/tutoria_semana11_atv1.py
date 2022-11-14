from biblioteca import*

print('Exercício 1 - Operações com Matriz')
print('----------------------------------')
dim = int(input('Qual a dimensão da matriz (n) ?'))

matriz = criarMatriz(dim, dim, 0)

print('Leitura dos elementos da matriz:')

for lin in range(dim):
    for col in range(dim):
        matriz[lin][col] = int(input(f'Elemento [{lin}][{col}] : '))

soma_prin = 0
prod_sec = 1
prod_acim = 1
tot_abaixo = 0
for lin in range(dim):
    for col in range(dim):
        if lin == col:
            soma_prin += matriz[lin][col]
        if lin + col + 1 == 4:
            prod_sec *= matriz[lin][col]
        if lin < col:
            prod_acim *= matriz[lin][col]
        if lin > col and matriz[lin][col] == 0:
            tot_abaixo += 1

print('Resultados')
print('----------')
print() 
print(f"Somatório (diagonal principal): {soma_prin:.2f}")

print(f"Produtório (diagonal secundária): {prod_sec:.2f}")

print(f"Produtório (acima da diagonal principal): {prod_acim:.2f}")

print(f"Nulos (abaixo da diagonal principal): {tot_abaixo}")           
            