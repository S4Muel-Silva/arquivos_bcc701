media = float(input('Média no semestre: '))
freq = int(input('Frequência no semestre: '))

if media >= 6:
    if freq >= 75:
        print('Conceito: aprovado')
    else:
        print('Conceito: reprovado por faltas')
        freq = 75 - freq
        print(f'Justificativa: frequência {freq}% abaixo da mínima')
else:
    if freq >= 75:
        print('Conceito: exame especial')
        media = 6 - media
        print(f'Justificativa: média {media:.2f} abaixo da mínima')
    else:
        print('Conceito: reprovado por faltas')
        freq = 75 - freq
        print(f'Justificativa: frequência {freq}% abaixo da mínima')        