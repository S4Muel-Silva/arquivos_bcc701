import math
print ('Transp Brasil')

r = float(input('Digite o raio do reservatório de combustível: '))

pi = math.pi
A = pi * r**2

h = float(input('Digite a altura do reservatório de combustível: '))

capac = float(input('Digite a capacidade (m3) de armazenamento de comb. dos caminhões: '))

volume = A*h

print(f'O volume do reservatório é {volume:.2f} m3.')

ncam = volume / capac
ncam = math.trunc(ncam)

print(f'{ncam} caminhões poderiam ser abastecidos com este reservatório')
