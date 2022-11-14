c1 = int(input('Cateto 1 (a): '))
c2 = int(input('Cateto 2 (b): '))
h = int(input('Hipotenusa (c): '))

if c1**2 + c2**2 == h**2:
    print(f'{c1}, {c2}, {h} representam um terno pitagórico')
else:
    print(f'{c1}, {c2}, {h} NÃO representam um terno pitagórico')