altura = float(input('Digite a altura: '))
sexo = input('Qual é o sexo (m ou f): ')

if sexo == 'm':
    ideal = (72.7*altura)-58
if sexo == 'f':
    ideal = (62.1*altura)-44.7
    
print(f'O peso ideal é {ideal:.2f}')