print('DEGEO - Projeto de extensão')

nome = input('Nome: ')

nota1 = float(input('Nota em GEO727: '))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input('Nota em GEO727: '))
    
nota2 = float(input('Nota em GEO451: '))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input('Nota em GEO451: '))
    
nota3 = float(input('Nota em GEO918: '))
while nota3 < 0 or nota3 > 10:
    nota3 = float(input('Nota em GEO918: '))
    
media = (nota1*2 + nota2*3 + nota3*4) / (2 + 3 + 4)

print(f'{nome} tem média {media:.2f}')

if media < 5:
    print('Não pode participar')
elif 5 <= media <= 6.5:
    print('Pode participar sem remuneração')
else:
    print('Pode participar com remuneração')
    