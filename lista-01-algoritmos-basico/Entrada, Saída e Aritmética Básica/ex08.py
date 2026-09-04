# 8. Área de um Triângulo: Crie um algoritmo que leia o valor da base e da altura de um triângulo, calcule e mostre a sua área (Fórmula: (base * altura) / 2).

print('Calculador de área de triângulos')

base = float(input('Insira a base do triângulo em cm: '))
altura = float(input('Insira a altura do triângulo em cm: '))
area = float(base * altura)/2
print('A área de um triângulo cuja base é {}cm e sua altura é {}cm é de {}cm².'.format(base, altura, area))
