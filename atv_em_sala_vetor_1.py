n_ava = int(input('Informe o número de avaliações: '))

sn = 'sim'
maior_media = 0
nome_maior =''
while sn == 'sim':
    
    soma_nota = 0
    soma_peso = 0
    
    nome = input('Nome do(a) aluno(a): ')
    
    for x in range(1, n_ava+1, 1):
        
        nota = float(input(f'Nota {x}: '))
        peso = int(input(f'Peso {x}: '))
        
        soma_nota += nota*peso
        soma_peso += peso
        
    media = soma_nota/soma_peso
    
    if media > maior_media:
        maior_media = media
        nome_maior = nome
        
    if media < 3:
        print(f'{nome} está reprovado(a) com média {media:.2f}')
    elif 3 <= media < 6:
        print(f'{nome} fará exame especial, média {media:.2f}')
    else:
        print(f'{nome} está aprovado(a) com média {media:.2f}')
    
    sn = input('Deseja avaliar outro aluno? (sim/nao) ')
    
print(f'{nome_maior} teve a maior média: {maior_media:.2f}')