# 7.  Área e Perímetro de Retângulo: Faça um algoritmo que leia a base e a altura de um retângulo. Calcule e mostre sua área (base * altura) e seu perímetro (soma dos 4 lados).

print('Calculador de Área e Perímetro de um Retângulo:')

base = float(input('Insira a base do retângulo em cm: '))
altura = float(input('Insira a altura do retângulo em cm: '))
area = float(base * altura)
perimetro = float( 2* (base + altura))
print('Um retângulo cuja base é {}cm e sua altura é {}cm, tem uma área de {}cm² e seu perímetro de {}cm.'.format(base, altura, area, perimetro))
