print('CÁLCULO DO IMPOTSO - DÓLAR AUSTRALIANO (AUD$)')

renda = int(input('DIGITE A RENDA TRIBUTÁVEL DO CIDADÃO: '))

if 0 < renda <= 6000:
    imp = 0

elif 6001 <= renda <= 20000:
    imp = (renda - 6000) * 0.17
    
elif 20001 <= renda <= 50000:
    imp = 2380 + (renda - 20000) * 0.30

elif 50001 <= renda <= 60000:
    imp = 11380 + (renda - 50000) * 0.42

else:
    imp = 15580 + (renda - 60000) * 0.47
    
imp_saude = 0.015*renda
imp_total = imp + imp_saude

print(f'RENDA TRIBUTÁVEL: AU$ {renda:.2f}')
print(f'IMPOSTO DEVIDO: AU$ {imp:.2f}')
print(f'IMPOSTO PARA A SAÚDE - Drunken Clam: AU$ {imp_saude:.2f}')
print(f'IMPOSTO TOTAL A SER PAGO: AU$ {imp_total:.2f}')
