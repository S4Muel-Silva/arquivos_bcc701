from biblioteca import*

def notasAlunos(vetor_gabarito, matriz_notas):
    qtlin, qtcol = dimMatriz(matriz_notas)
    n_quest = len(vetor_gabarito)
    vetor_res = []
    
    for lin in range(qtlin):
        calc_nota = 0
        for col in range(qtcol):
            
            if matriz_notas[lin][col] == vetor_gabarito[col]:
                calc_nota += 1
                
        calc_nota = (calc_nota*10) / n_quest
        calc_nota = round(calc_nota, 1)
        vetor_res.append(calc_nota)
        
    return vetor_res

print('Notas de BCC701')
vetor_gabarito = inputVetor('Digite o gabarito: \n>>> ', str)

matriz_notas = inputMatriz('Digite as respostas dos alunos: \n>>>', str)

qtlin, qtcol = dimMatriz(matriz_notas)

if matriz_notas == [ ]:
    print('Nenhum aluno para avaliar')
    
elif qtcol != len(vetor_gabarito):
    print('Quantidade de questões incompatível')

else:
    vetor_res = notasAlunos(vetor_gabarito, matriz_notas)
    
    print('Notas dos alunos:')
    print(vetor_res)
    

    