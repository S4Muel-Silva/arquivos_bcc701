def Primo (a):
    x = 2
    y = a
    while x < y:
        if y % x == 0:
            return False
        else:
            x += 1
        return True

x = int(input('numero: '))
while x > 0:
    res = Primo(x)
    if res == True:
        print(f'{x} é primo')
    else:
        print(f'{x} não é primo')
    x = int(input('numero: '))
    