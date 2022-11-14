print('TABELA DA FUNÇÃO')
print('x/y', end = '')
cont = 0
for x in range(1, 9, 1):
    print(f'{x:6d}', end = '')
    cont += 1
print()
print('-'*(6*cont+4))

x = 8
for x in range(1, x+1, 1):
    print(f'{x} |', end = '')
    for y in range(1, x+1, 1):
        if x==y:
            valor = (x*y)/(x+y)
        elif (x+y)%2 != 0:
            valor = (x**2)+(y**2)
        else:
            valor = x+y
        
        print(f'{valor:6.1f}', end = '')
    print()

