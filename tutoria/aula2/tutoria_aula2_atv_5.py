print('Cálculo do IPTU - Prefeitura de Ouro Preto\n------------------------------------------')

tipo = int(input('Tipo de lote (1 ou 2): '))

if tipo != 1 and tipo != 2:
    print('ERRO: Tipo de lote inválido!')
    print('Fim do Programa')
    quit()
else:
    area = float(input('Área do imóvel (m2): '))
    
    if tipo == 1:
        if 0 < area < 200:
            iptu = area*1.0
        if area >= 200:
            iptu = area*1.2
    else:
        if 0 < area < 200:
            iptu = area*1.1
        if area >= 200:
            iptu = area*1.3
    print(f'O valor do IPTU é R${iptu:.2f}')
    print('Fim do Programa')