from biblioteca import*

print('Exercício 2 - Modificação de uma Coluna da Matriz')
print('-------------------------------------------------')

matriz = inputMatriz('Digite toda a matriz de inteiros \n>>> ', int)

qtlin, qtcol = dimMatriz(matriz)

escalar = int(input('Digite uma constante: '))

mod_col = int(input('Índice de uma coluna: '))

while mod_col >= qtlin:
    mod_col = int(input('Índice de uma coluna: '))
    
for lin in range(qtlin):
    for col in range(qtcol):
        
        if col == mod_col:
            matriz[lin][col] *= escalar

print('Resultados')
print('----------')

print('Matriz Resultante:')
for lin in range(qtlin):
    print()
    for col in range(qtcol):
        print(f'{matriz[lin][col]:8.2f}', end = '')