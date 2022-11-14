print('1 - Celcius para Fahrenheit\n2 - Fahrenheit para Celcius')

opcao = int(input('Informe a opção desejada: '))

if opcao == 1:
    temp_celcius = float(input('Informe a temperatura em Celcius: '))
        
    temp_fah = (temp_celcius / 5) * 9 + 32
        
    print(f' A temperatura em Fahrenheit é {temp_fah}')
    
elif opcao == 2:
    temp_fah = float(input('Informe a temperatura em Fahrenheit: '))
        
    temp_celcius = ((temp_fah - 32) / 9) * 5
        
    print(f' A temperatura em Celcius é {temp_celcius}')
else:
    print('Opção inválida!')