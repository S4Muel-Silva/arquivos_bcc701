def lucroVendedor(bolinhos, suco, lucro_bolinho, lucro_suco):
    lucro = []
    
    for x in range(len(bolinhos)):
        lucro.append(bolinhos[x]*lucro_bolinho + suco[x]*lucro_suco)
    return(lucro)
bolinhos = []
suco = []
lucro = []

valores = input('Bolinhos: ')
valores = valores.split(',')
for i in range(len(valores)):
    valor = conversao(valores[i].strip())
    resultado.append(valor)

valores = input('Suco: ')
valores = valores.split(',')
for i in range(len(valores)):
    valor = conversao(valores[i].strip())
    resultado.append(valor)


lucro_bolinho = float(input('Lucro com bolinho: '))
lucro_suco = float(input('Lucro com suco: '))

lucro = lucroVendedor(bolinhos, suco, lucro_bolinho, lucro_suco)

print('O lucro dos vendedores foi: ')
maior_lucro = 0

for x in range(1, len(lucro)+1, 1):
    print(f'{x}: lucro[x]')
    
    if lucro[x] > lucro:
        maior_lucro = x

print(f'O vencedor premiado foi o {maior_lucro}')
    
    