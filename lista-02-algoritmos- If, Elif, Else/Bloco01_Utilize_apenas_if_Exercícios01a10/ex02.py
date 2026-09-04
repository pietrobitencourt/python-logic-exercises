# 2) Número positivo. Leia um número inteiro e exiba "O número é positivo." se ele for maior que zero.

numero = int(input('Digite um número: '))
if numero > 0:
    print('Esse número é positivo!')
elif numero == 0:
    print('Esse número é neutro!')
else:
    print('Esse número é negativo!')
