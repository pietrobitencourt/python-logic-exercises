# 3. Dobro e Terça Parte: Crie um algoritmo que leia um número real. Calcule e mostre o seu dobro (multiplicação) e a sua terça parte (divisão por 3).

num1 = int(input('Digite um número: '))
dobro = int(num1 * 2)
terca_parte = float(num1 / 3)
print('O dobro de {} é {} e sua terça parte é {}.'.format(num1, dobro, terca_parte))
