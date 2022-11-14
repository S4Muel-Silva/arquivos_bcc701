import math

def minimo (a, b):
    if a < b:
        return a
    else:
        return b
    
def maximo (a, b):
    if a > b:
        return a
    else:
        return b

def calcDano (a, b, d):
    dano = minimo(999, math.trunc(a*(1+b)*(1-d/(100+d))))
    return dano
    
def vidaAposGolpe (v, a, b, d):
    vida = maximo(0, v-calcDano(a, b, d))
    return vida

p1 = int(input('Força de ataque do personagem 1: '))
p2 = int(input('Força de ataque do personagem 2: '))
p3 = int(input('Força de ataque do personagem 3: '))
p4 = int(input('Força de ataque do personagem 4: '))

defesaInimigo = int(input('Força de defesa do inimigo: '))
vidaInimigo = int(input('Vida inicial do inimigo: '))

recebido = vidaAposGolpe(vidaInimigo, p1, 0.15, defesaInimigo)
recebido = vidaAposGolpe(recebido, p2, 0, defesaInimigo)
recebido = vidaAposGolpe(recebido, p3, 0, defesaInimigo)
recebido = vidaAposGolpe(recebido, p4, 0.15, defesaInimigo)

print(f'A vida do inimigo será: {recebido}')