cont = int(input('Digite o número de alunos: '))
media_turma = 0

for i in range(1, cont+1, 1):
    nome = input(f'Digite o nome do aluno {i}: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    
    media = (nota1*2 + nota2*3 + nota3*5) / (2 + 3 + 5)
    
    media_turma = media_turma + media
    
    print(f'Média Ponderada das notas de {nome}: {media:.3f}')
print(f'Média da turma: {media_turma/3:.3f}')