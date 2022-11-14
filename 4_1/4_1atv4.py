nome = input('Entre com o nome: ')
idade = float(input('Entre com a idade: '))
sexo = input('Entre com o sexo (m ou f): ')

if sexo == 'm':
    if idade >= 18:
        print(f'{nome} tem maioridade civil')
    else:
        resta = 18 - idade
        print(f'Faltam {resta:.1f} anos para {nome} atingir a maioridade')
if sexo == 'f':
    if idade >= 21:
        print(f'{nome} tem maioridade civil')
    else:
        resta = 21 - idade
        print(f'Faltam {resta:.1f} anos para {nome} atingir a maioridade')
