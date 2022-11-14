def Distancia(v, t):
    d = v*t
    return d

def Litros(d):
    L = d/12
    return L

print('Consumo na Viagem')
v = float(input('Velocidade Média (km/h): '))
t = float(input('Tempo de viagem (h): '))

dis = Distancia(v, t)
res = Litros(dis)

print(f'Combustível gasto (l): {res:.2f}')