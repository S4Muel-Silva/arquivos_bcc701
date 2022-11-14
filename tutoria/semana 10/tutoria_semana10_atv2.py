print('Exercício 2 - Temperaturas em Chicago e São Francisco')

tch = [75,79,86,86,79,81,73,89,91,86,81,82,86,88,89,90,82,84,81,79,73,69,73,79,82,72,66,71,69,66,66]
tsf = [69,79,70,73,72,71,69,76,85,86,74,84,76,68,79,75,68,68,73,72,79,68,68,69,71,70,89,95,90,66,69]
vetor_res = []
for x in range(len(tch)):
    if tch[x] == tsf[x]:
        vetor_res.append(x+1)
print(f'Quantidade de dias com a mesma temperatura: {len(vetor_res)}')
print('Datas de Agosto:')
for x in range(len(vetor_res)):
    print(f'{vetor_res[x]} ', end='')