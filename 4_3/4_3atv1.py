m14 = float(input('Média móvel dos últimos 14 dias: '))
a6 = int(input('Somatório dos casos dos últimos 6 dias: '))
h = int(input('Quantidade de casos hoje: '))

m7 = (a6+h)/7

d = m7 - m14
crescimento = d/m14*100

if crescimento < 0:
    crescimento = abs(crescimento)
    print(f'Casos diminuindo em {crescimento:.2f}%')
else:
    if crescimento < 15:
        print(f'Casos estáveis em {crescimento:.2f}%')
    else:
        print(f'Casos aumentando em {crescimento:.2f}%')