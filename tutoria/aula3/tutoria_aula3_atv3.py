a = int(input('DIGITE O PRIMEIRO ÂNGULO INTERNO: '))
b = int(input('DIGITE O SEGUNDO ÂNGULO INTERNO: '))
c = int(input('DIGITE O TERCEIRO ÂNGULO INTERNO: '))

if a + b + c != 180:
    print('TRIÂNGULO INEXISTENTE')
else:
    if a == 90 or b == 90 or c == 90:
        print('TRIÂNGULO RETÂNGULO')
    if a > 90 or b > 90 or c > 90:
        print('TRIÂNGULO OBTUSÂNGULO')
    if a < 90 and b < 90 and c < 90:
        print('TRIÂNGULO ACUTÂNGULO')