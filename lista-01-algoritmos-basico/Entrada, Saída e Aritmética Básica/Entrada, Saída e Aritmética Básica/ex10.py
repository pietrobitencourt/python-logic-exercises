# 10. Conversão de Temperatura: Escreva um algoritmo que leia uma temperatura em graus Celsius e a converta para Fahrenheit (Fórmula: F = (C * 9/5) + 32).

print('---Convertor de Temperatura---')

temperatura = float(input('Insira a temperatura em graus Celsius(℃): '))
fahrenheit = float((temperatura * (9 / 5)) + 32)
print('A conversão da temperatura {}℃ para Fahrenheit é de: {}℉.'.format(temperatura, fahrenheit))
