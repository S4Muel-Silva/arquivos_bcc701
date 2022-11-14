P = float(input('Digite a pressão (em atm) : '))
C = float(input('Digite a temperatura (em graus Celcius) : '))

K = C + 273.15
T = K
n = 3
R = 0.082
V = (n * R * K) / P
print(f'{n} mols de um gás a {C} graus Celcius e a {P} atm, ocupam {V:.4f}')