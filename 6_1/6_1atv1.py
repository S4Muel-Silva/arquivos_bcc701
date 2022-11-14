def avaliaTubo (comp, desejado, erro):
    if desejado - comp > erro or comp - desejado > erro:
        return False
    else:
        return True
    
cont = 0
cortados = 0
rejeitados = 0

comp_desejado = float(input('Comprimento de corte dos tubos: '))
marg_erro = float(input('Margem de erro aceitável: '))
quant = int(input('Quantidade de tubos demandada: '))

while cont < quant:
    comp_real = float(input('Coprimento do tubo cortado: '))
    
    res = avaliaTubo(comp_real, comp_desejado, marg_erro)
    
    if res == True:
        cortados = cortados + 1
        cont = cont + 1
    else:
        cortados = cortados + 1
        rejeitados = rejeitados + 1
        print('Acima da margem de erro, tubo rejeitado')
        
print('Fim da produção. demanda atendida')    
print(f'Total de tubos cortados: {cortados}')
print(f'Total de tubos rejeitados: {rejeitados}')
    
    

    
        