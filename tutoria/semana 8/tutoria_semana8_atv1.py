import math
print("x/y |    3     6     9     12    15    18    21    24")
print('-'*54)

y = 24
x = 30

for i in range(2, x+1, 2):
    print (f'{i:3.0f} |', end = ' ')
    for j in range(3, y+1, 3):
        if (i+j)%2 == 0:
            a = (1/(i*j)) + math.sin(i+j)
        elif (i*j)%2 != 0:
            a = ((j**2)-(4*i))**(1/2)
        else:
            a = (i+j)**(1/3)
        print(f'{a:5.2f}', end = ' ')
    print(' ')
            