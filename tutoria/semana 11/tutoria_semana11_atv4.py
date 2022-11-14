from biblioteca import*

print('Exercício 4 - Imagem em Preto e Branco')
print('--------------------------------------')

matriz = inputMatriz('Digite a matriz da imagem, todos os elementos: \n>>> ', int)
qtlin, qtcol = dimMatriz(matriz)

print('Resultados')
print('--------------------------------------')

print('Imagem:')
for lin in range(qtlin):
    print()
    for col in range(qtcol):
        print(f'{matriz[lin][col]:6.2f}', end='')   
print()
print()

print('Negativo:')

for lin in range(qtlin):
    print()
    for col in range(qtcol):
        
        if matriz[lin][col] == 0:
            matriz[lin][col] = 1
            print(f'{matriz[lin][col]:6.2f}', end='')
        else:
            matriz[lin][col] = 0
            print(f'{matriz[lin][col]:6.2f}', end='')