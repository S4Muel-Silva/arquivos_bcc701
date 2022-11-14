def realizaCalculos(termos, raio):
    pi = 0
    for i in range(0, termos, 1):
        
        pi += (-1)**i*(4/(2*i+1))
    
    v = (4/3)*pi*(raio**3)
    pi = round(pi, 5)
    v = round(v, 5)
    return(pi, v)

termos = int(input('Número de termos: '))

raio = float(input('Raio da esfera: '))
    
(res1, res2) = realizaCalculos(termos, raio)

print(f'pi = {res1}.')
print(f'Volume da esfera = {res2}.')