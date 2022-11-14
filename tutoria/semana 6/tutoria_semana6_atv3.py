obs_ext = 0
mag_ext = 0

cont = int(input('Quantidade de participantes: '))

for i in range(1, cont+1, 1):
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    
    imc = peso / (altura**2)
    
    if imc < 16:
        estado = 'Magreza grave'
        mag_ext += 1
    elif 16 <= imc < 18.5:
        estado = 'Abaixo do peso'
    elif 18.5 <= imc < 25:
        estado = 'Saudável'
    elif 25 <= imc < 30:
        estado = 'Sobrepeso'
    elif 30 <= imc < 40:
        estado = 'Obesidade'
    else:
        estado = 'Obesidade extrema'
        obs_ext += 1
        
    print(f'O IMC é {imc:.2f} ==> {estado}\n')
    
oep = (obs_ext/cont)*100
mep = (mag_ext/cont)*100

print(f'Percentual para Magreza grave: {mep:.2f}')
print(f'Percentual para Obesidade extrema: {oep:.2f}')

