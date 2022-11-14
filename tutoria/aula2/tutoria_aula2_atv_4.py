print('Cálculo da Energia Elétrica\n---------------------------')

consumo = int(input('Digite o consumo de Energia Elétrica (KW): '))

print('---------------------------')

if consumo <= 0:
    print('ERRO: o consumo deve ser inteiro e positivo (não nulo)')
    print('Fim do Programa')
    quit()
else:
    taxa1 = 5.00
    print(f'Taxa básica: R${taxa1}')
    
    if consumo > 0 and consumo < 500:
        tarifa1 = consumo*0.02 + consumo
    elif 500 < consumo <= 1000:
        tarifa1 = 10.00 + (consumo-500)*0.05
    else:
        tarifa1 = 35.00 + (consumo-1000)*0.1

print(f'consumo (k): {consumo}')

valor_conta = taxa1 + tarifa1

print(f'Valor da conta: R${valor_conta:.2f}')

print('Fim do Programa')

