vendedor = [ "Megan", "Peter", "Lois", "Stewie", "Brian" ]
sapato = [ 8, 6, 30, 12, 11 ]
camisa = [ 25, 25, 22, 10, 40 ]

print('Exercício 3 - Loja Quahog Crazy Store')
print()
print('Resultados')
print()

mais_sapatos = 0
ind1 = 0
menos_camisas = 100000
ind2 = 0
camp_vendas = 0
ind3 = 0

for x in range(len(vendedor)):
    valor1 = sapato[x]
    valor2 = camisa[x]
    if valor1 > mais_sapatos:
        mais_sapatos = valor1
        ind1 = x
    if valor2 < menos_camisas:
        menos_camisas = valor2
        ind2 = x
    if sapato[x]+camisa[x] > camp_vendas:
        camp_vendas = sapato[x]+camisa[x]
        ind3 = x

print(f'Maior Vendedor de sapatos: {vendedor[ind1]}')
print(f'Quantidade de sapatos: {sapato[ind1]}')
print()

print(f'Vendedor Lanterna de camisas: {vendedor[ind2]}')
print(f'Quantidade de camisas: {camisa[ind2]}')
print()

print(f'Campeão de vendas no mês: {vendedor[ind3]}')
print(f'Quantidade de vendas: {camisa[ind3]+sapato[ind3]}')

print(f'Quantidade de sapatos: {sapato[ind3]}')
print(f'Quantidade de camisas: {camisa[ind3]}')