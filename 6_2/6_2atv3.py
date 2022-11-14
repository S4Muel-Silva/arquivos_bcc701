c1 = input('Nome do candidato 1: ')
n1 = int(input('Número do candidato 1: '))

c2 = input('Nome do candidato 2: ')
n2 = int(input('Número do candidato 2: '))

v1 = 0; v2 = 0; vi = 0; vv = 0

eleit = int(input('Quantidade de eleitores: '))
while eleit < 3:
    print('A quantidade de eleitores é inferior a 3')
    eleit = int(input('Quantidade de eleitores: '))
    
print('\n## Votação Iniciada')
for i in range(1, eleit+1, 1):
    voto = int(input('Número do candidato que deseja votar: '))
    if voto == n1:
        v1 += 1
        vv += 1
    elif voto == n2:
        v2 += 1
        vv += 1
    else:
        vi += 1
print('## Votação Encerrada\n')

vvp = (vv/eleit)*100
vip = (vi/eleit)*100

if vv !=0:
    v1p = ((v1)/vv)*100
    v2p = ((v2)/vv)*100
else:
    v1p = 0
    v2p = 0
    
print(f'Votos válidos: {vvp:.2f}% ({vv} votos)')
print(f'Votos inválidos: {vip:.2f}% ({vi} votos)')
print(f'Votos para {c1}: {v1p:.2f}% ({v1} votos)')
print(f'Votos para {c2}: {v2p:.2f}% ({v2} votos)')