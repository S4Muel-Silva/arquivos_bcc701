import math
def impostoRenda (a):
    if a <= 1500:
        D = 0
    elif 1500 < a <= 2500:
        D = 0.05*a
    elif 2500 < a <= 4500:
        D = 0.1*a
    else:
        D = 0.2*a
    return round(D, 2)

B = float(input('Digite o salário bruto: '))
IR = impostoRenda(B)

print(f'(-)IR: R$ {IR:.2f}')

INSS = 0.1*B

print(f'(-)INSS: R$ {INSS:.2f}')

FGTS = 0.11*B

print(f'FGTS: R$ {FGTS:.2f}')

print(f'Total de descontos: R$ {IR+INSS:.2f}')

print(f'Salário Líquido: R$ {B-IR-INSS:.2f}')