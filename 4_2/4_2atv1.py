C = float(input('Capital emprestado: '))
m = int(input('Quantidade de meses para quitação: '))

if C <= 10000:
    t = 0.1
else:
    t = 0.07

print(f'Taxa de juros aplicada: {t*100:.0f}%')

J = C*t*m

print(f'Juros devido: {J:.2f}')
print(f'Valor total: {C+J:.2f}')
