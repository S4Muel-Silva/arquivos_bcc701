def converteMedidas (M):
    FT = 0.3048*M
    YD = 0.9144*M
    
    FT = round(FT, 3)
    YD = round(YD, 3)
    
    return (FT, YD)

print('Percurso 1:')

M1 = float(input('- Tamanho em metros: '))
a1, b1 = converteMedidas(M1)

print(f'- Tamanho em pés...: {a1:.2f}')
print(f'- Tamanho em jardas: {b1:.2f}')

print('Percurso 2:')

M2 = float(input('- Tamanho em metros: '))
a2, b2 = converteMedidas(M2)

print(f'- Tamanho em pés...: {a2:.2f}')
print(f'- Tamanho em jardas: {b2:.2f}')



print('Percurso 3:')

M3 = float(input('- Tamanho em metros: '))
a3, b3 = converteMedidas(M3)

print(f'- Tamanho em pés...: {a3:.2f}')
print(f'- Tamanho em jardas: {b3:.2f}')