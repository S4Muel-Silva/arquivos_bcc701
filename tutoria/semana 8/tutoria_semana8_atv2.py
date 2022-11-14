sn = input('Deseja calcular a Sequência de Collatz (s/S/n/N) ?')

while sn != 's' and sn != 'S' and sn != 'n' and sn != 'N':
    sn = sn.upper()
    print(f'ERRO: Resposta inválida: {sn}')
    
    sn = input('Deseja calcular a Sequência de Collatz (s/S/n/N) ?')
    

while sn == 's' or sn == 'S':
    num = int(input('Digite um número inteiro positivo: '))
            
    print('Sequencia de Collatz: ')
    
    print(num, end = ' ')
    while num != 1:
        if num%3 == 0:
            num = num/3
        elif num%3 == 1:
            num = ((4*num+2)/3)
        elif num%3 == 2:
            num = ((2*num-1)/3)
        print(f'{num:.0f}', end = ' ')
    sn = input('\nDeseja calcular a Sequência de Collatz (s/S/n/N) ?')

    while sn != 's' and sn != 'S' and sn != 'n' and sn != 'N':
        sn = sn.upper()
        print(f'ERRO: Resposta inválida: {sn}')
        
        sn = input('Deseja calcular a Sequência de Collatz (s/S/n/N) ?')
            
print('Fim do Programa!')
        
        
            
            