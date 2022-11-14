aluno = [ "Peny", "Rajesh Koothrappali", "Sheldon Cooper", "Howard Wolowitz", "Leonard Hofstadter" ]
notasBCC701 = [ 6.0, 8.5, 10.0, 9.0, 9.5 ]

print('Buscando a nota de um aluno...')
busca = input('Digite o nome do(a) aluno(a): ')
k = -1
for i in range(5):
    nomes = aluno[i]
    if nomes == busca:
        k = i
        nota = notasBCC701[i]
if k == -1:
    print('Erro na busca, aluno(a) não encontrado(a) !')
else:
    print('Resultados:')
    print(f'Nome do(a) aluno(a) buscado(a): {aluno[k]}')
    print(f'Nota: {nota}')