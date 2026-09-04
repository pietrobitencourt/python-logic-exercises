# 11. Cálculo de IMC: Leia o peso (kg) e a altura (m) de uma pessoa e calcule o seu IMC. (Fórmula: IMC = peso / (altura * altura)).

print('-Calculador de IMC (simples)-')
peso = float(input('Qual o seu peso (kg)? '))
altura = float(input('Qual a sua altura (em metros)? '))
imc = peso / (altura ** 2)
print('O seu IMC é de {}!'.format(imc))
