verifica = 'sim'
menos21 = 0
cont = 0
media = 0
while verifica == 'sim':
    nome = input('nome: ')
    idade = int(input('idade: '))
    
    if idade <= 21:
        menos21 += 1
        cont += 1
        media += idade
    else:
        cont += 1
        media += idade
    
    verifica = input('Mais uma pessoa? (sim/nao): ')
    
    while verifica != 'sim' and verifica != 'nao':
        verifica = input('Mais uma pessoa? (sim/nao): ')

media = media/cont
menos21 = (menos21/cont) * 100

print (media)
print (menos21)
        

