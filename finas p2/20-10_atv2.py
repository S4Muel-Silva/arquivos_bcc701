from biblioteca import *
print("Loja da tia Maria")

Mat = inputMatriz("Matriz de estoque: ", int)
At = int(input("Numero de atualizações: "))
for x in range(At):
    IndLoja = int(input("Índice da loja: "))
    IndProd = int(input("Índice do produto: "))
    NvEstoq = int(input("Novo estoque: "))
    
    Mat[IndLoja][IndProd] = NvEstoq
                
    for lin in range(len(Mat)):
        print(Mat[lin])