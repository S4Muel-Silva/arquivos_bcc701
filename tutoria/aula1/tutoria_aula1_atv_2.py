s1 = float(input('DIGITE O LADO 1 DO TRIÂNGULO (m) : '))
s2 = float(input('DIGITE O LADO 2 DO TRIÂNGULO (m) : '))
s3 = float(input('DIGITE O LADO 3 DO TRIÂNGULO (m) : '))

s = (s1 + s2 + s3) / 2

area = (s * (s - s1) * (s - s2) * (s - s3) ) ** (1/2)

per = s1 + s2 + s3

print(f'PERÍMETRO DO TRIÂNGULO = {per:.0f} m')
print(f'ÁREA DO TRIÂNGULO = {area:.4f} m')