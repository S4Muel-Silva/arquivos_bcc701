def calculo (num):
    x = 1
    soma = 0    
    while num > x:
        if num % x == 0:
            soma = soma + x
            x = x + 1
        else:
            x = x + 1
    return (soma)

cont = 1
numero = int(input('Digite um número: '))

if numero > 0:
    while numero > cont:
        
        res = calculo(numero)
        
        if numero == res:
            print(f'{numero} == {res}: número é perfeito')
        else:
            print(f'{numero} <> {res}: número não é perfeito')
            
        numero = int(input('Digite um número: '))
        
    #print (x)
    #print (soma)
