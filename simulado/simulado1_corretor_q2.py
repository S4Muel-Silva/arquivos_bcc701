def calc (produto, valor):
    if produto == 1:
        if valor <= 50:
            desconto = 0.1
        elif 50 < valor <= 100:
            desconto = 0.12
        else:
            desconto = 0.15
        
        return desconto
    
    if produto == 2:
        if valor <= 50:
            desconto = 0.09
        elif 50 < valor <= 100:
            desconto = 0.1
        else:
            desconto = 0.11
        
        return desconto

produto = input('Informe o nome do produto: ')

while produto != 'fim':
    if produto == 'Pão de queijo':
        cp = 1
    elif produto == 'Pastel de angu':
        cp = 2
    else:
        print('Erro')
        
    valor = float(input('Valor do pedido: R$ '))
    
    
    desconto = calc(cp, valor)
    valor_desc = valor - valor * desconto
    desconto = desconto*100
    
    print(f'Percentual de desconto: {desconto:.2f}%')
    print(f'Valor com desconto: R$ {valor_desc:.2f}')
    
    produto = input('Informe o nome do produto: ')