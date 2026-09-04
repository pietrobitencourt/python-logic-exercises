# 5) Velocidade acima do limite. Leia a velocidade de um veículo (km/h). Se ultrapassar 80 km/h, exiba "Velocidade acima do limite!".

velocidade = float(input('Qual a velocidade do veículo (em km/h)? '))
if velocidade > 80:
    print('Velocidade acima do limite!')
else:
    print('Velocidade abaixo do limite!')
