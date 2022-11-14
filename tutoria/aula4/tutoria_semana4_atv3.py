import math

def potencia (a, b):
    x = 10**(b*math.log10(a))
    return x

print('Cálculo da Potência')

base = float(input('Valor da base (A): '))
expo = float(input('Valor do expoente (B): '))

res = potencia(base, expo)

print(f'A**B: {res:.2f}')