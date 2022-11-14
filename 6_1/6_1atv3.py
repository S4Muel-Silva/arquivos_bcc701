def calculaJ (C, m):
    if C <= 10000:
        t = 0.1
    else:
        t = 0.07
    J = C*t*m
    return J, t*100
    
T = float(input('Capital Total para empréstimo: '))
C = float(input('Capital emprestado: '))

teste = True
while teste == True:
    if T < C:
        print(f'Empréstimo negado, capital total é de R$ {T:.2f}')
        teste = False
    else:
        m = int(input('Quantidade de meses para quitação: '))
        
        (devido, juros) = calculaJ(C, m)
        
        print(f'Taxa de juros aplicada: {juros:.0f}%.')
                
        print(f'Juros devido: {devido:.2f}.')
        total = C + devido
        print(f'Valor total: {total:.2f}.')
        T = T - C
        
        C = float(input('Capital emprestado: '))
        
        
        
        