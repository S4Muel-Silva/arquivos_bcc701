anos = int(input('Anos de experiência: '))
lings = int(input('Linguagens de programação: '))
projs = int(input('Projetos: '))

if anos >= 10 and lings >= 5 and projs >= 10:
    print('Concorrendo à Vaga Sênior')
    
elif anos >= 3 and lings >= 3 and projs >= 5:
    anos = 10 - anos
    lings = 5 - lings
    projs = 10 - projs
    
    print('Concorrendo à Vaga Pleno. Para concorrer à Vaga Sênior, faltam:')
    
    if anos > 0:
        print(f'- {anos} anos de experiência')
    if lings > 0:
        print(f'- {lings} linguagens de programação')
    if projs > 0:
        print(f'- {projs} projetos')
else:
    
    anos = 3 - anos
    lings = 3 - lings
    projs = 5 - projs
    
    print('Concorrendo à Vaga Júnior. Para concorrer à Vaga Pleno, faltam:')
    
    if anos > 0:
        print(f'- {anos} anos de experiência')
    if lings > 0:
        print(f'- {lings} linguagens de programação')
    if projs > 0:
        print(f'- {projs} projetos')