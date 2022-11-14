def avaliaApresentação (juizes):
    #1
    grau = float(input('. Grau de dificuldade: '))
    #2
    cont = 1
    nota = 0
    while cont <= juizes:
        nota = nota + float(input(f'. Nota do juíz {cont}: '))
        cont = cont + 1
    #3
    print(f'. Pontuação da apresentação: {nota*grau:.2f}')
    
    

cont = 1
quant = int(input('Defina a quantidade de apresentações: '))
juizes = int(input('Defina a quantidade de juízes: '))

while quant >= cont:
    
    print(f'. Apresentação {cont}:')
    
    avaliaApresentação (juizes)
    
    cont = cont + 1