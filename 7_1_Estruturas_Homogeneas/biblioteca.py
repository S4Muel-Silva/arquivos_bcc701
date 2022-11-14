#criarVetor: Cria um vetor com valor padrão
#    Argumentos de entrada:
#        qtdElementos: Quantidade de elementos
#        valorPadrao: Valor padrão
#    Valor de retorno:
#        vetor: Um vetor contendo a quantidade de elementos armazenando o valor padrão

def criarVetor(qtdElementos, valorPadrao):
    vetor = [ ]
    for i in range(qtdElementos):
        vetor.append(valorPadrao)
    return vetor

#inputVetor: Cria um vetor com valores em uma string
#    Argumentos de entrada:
#        mensagem: Mensagem para a entrada do usuário
#        conversao: Função de conversão de tipo
#    Valor de retorno:
#        resultado: Um vetor com os valores extraı́dos da string fornecida pelo usuário e convertidos para o tipo definido

def inputVetor(mensagem, conversao):
    valores = input(mensagem)
    resultado = [ ]
    if valores == '':
        return resultado
    valores = valores.split(',')
    for i in range(len(valores)):
        valor = conversao(valores[i].strip())
        resultado.append(valor)
    return resultado