alunos = int(input('Quantidade de alunos: '))
disciplinas = int(input('Quantidade de disciplinas: '))
vetor = []
for i in range(alunos):
    print(f'\nDados do aluno {i + 1}:')
    d =[]
    for j in range(disciplinas):
        info = {}
        print(f'- Dados da disciplina {j + 1}:')
        info["Nota"] = float(input('- Nota: '))
        info["Freq"] = int(input('- Frequência: '))
        d.append(info)
    vetor.append(d)
print('\nDados das disciplinas com maiores notas:')
for i in range(alunos):
    maior = 0
    for j in range(1, disciplinas):
        if vetor[i][j]["Nota"] > vetor[i][maior]["Nota"]:
            maior = j
    print(f'- Aluno {i+1}: nota = {vetor[i][maior]["Nota"]}; frequência = {vetor[i][maior]["Freq"]}')