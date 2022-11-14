print('Custo do combustível em uma viagem')

def Custo (v, t, r, p):
    c = (v * t / r) * p
    c = round (c, 2)
    return c

v = float(input('Velocidade média (km/h): '))
t = float(input('Tempo previsto (h): '))
rg = float(input('Rendimento com gasolina (km/litro): '))
pg = float(input('Preço do litro de gasolina (R$): '))
pa = float(input('Preço do litro do álcool (R$): '))

ra = 0.7 * rg

cg = Custo (v, t, rg, pg)
ca = Custo (v, t, ra, pa)

print(f'Custo usando gasolina (R$): {cg:.2f}')
print(f'Custo usando álcool (R$): {ca:.2f}')