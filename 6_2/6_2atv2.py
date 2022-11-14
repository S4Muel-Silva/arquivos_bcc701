m_i = 0
m_f = 0
m_c = 0
m_t = 0

nome = input('Informe o nome do juiz: ')
part = int(input('Quantidade de partidas: '))

for i in range(1, part+1, 1):
    
    print(f'\nPartida {i}:')
    
    m_i += int(input('. Impedimentos.......: '))
    m_f += int(input('. Faltas.............: '))
    m_c += int(input('. Cartões............: '))
    m_t += float(input('. Tempo de acréscimo.: '))

m_i /= i
m_f /= i
m_c /= i
m_t /= i

print(f'\nEstatísticas do juiz {nome}:')

print(f'. Impedimentos.......: {m_i:.2f}.')
print(f'. Faltas.............: {m_f:.2f}.')
print(f'. Cartões............: {m_c:.2f}.')
print(f'. Tempo de acréscimo.: {m_t:.2f}.')