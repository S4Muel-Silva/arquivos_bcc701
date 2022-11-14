peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))
sexo = input('Seu sexo é masculino (M) ou feminino (F)? ')

imc = peso/(altura**2)

if sexo == 'M' or sexo == 'm':
    
    if imc > 25:
        peso = peso - 25*(altura**2)
        print(f'Você deve perder {peso:.2f}kg para ter IMC = 25')
    else:
        print('Você não precisa perder peso para ter IMC <= 25')

elif sexo =='F' or sexo == 'f':
    
    if imc > 24:
        peso = peso - 24*(altura**2)
        print(f'Você deve perder {peso:.2f}kg para ter IMC = 24')
    else:
        print('Você não precisa perder peso para ter IMC <= 24')

else:
    print('A entrada contém dados não reconhecidos')