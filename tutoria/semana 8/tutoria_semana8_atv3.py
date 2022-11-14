import math
sair = 'n'

while sair == 'n' or sair == 'N':
    tempk = float(input('Informe a temperatura (em Kelvin): '))
    print('Tensão | Corrente')
    for x in range(-100, 70, 10):
        print(f'{x/100:6.1f} |', end = '')
        
        x = x/100
            
        vd = x
        i0 = 2.0*(10**(-6) )
        q = 1.602*(10**(-19) )
        k = 1.38*(10**(-23) )
        t = tempk
            
        pot = (q*vd)/(k*t)
            
        corrente = i0*( (math.e**pot) -1)
            
        print(f' {corrente:.1f}', end = '')
        print()
    sair = input('Deseja sair? (s/S/n/N): ')
    while sair != 's' and sair != 'S' and sair != 'n' and sair != 'N':
        print(f'ERRO: opção inválida ! {sair}')
        sair = input('Deseja sair? (s/S/n/N): ')