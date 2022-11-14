def Fatorial (n):
    cont = 1
    fatorial = n
    while cont < n and cont <= n:
        fatorial = fatorial*(n - cont)
        cont = cont + 1
    return fatorial

valor = int(input('Informe o número que deseja calcular o Fatorial: '))

while valor <= 0:
    valor = int(input('Número inválido, defina outro: '))

res = Fatorial(valor)

print(f'O Fatorial de {valor} é: {res}')
        
        
    