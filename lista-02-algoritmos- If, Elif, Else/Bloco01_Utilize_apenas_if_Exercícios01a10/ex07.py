# 7) Maior entre dois números. Leia dois números inteiros. Se o primeiro for maior que o segundo, exiba "O primeiro número é maior.".

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
if numero_1 > numero_2:
    print('O primeiro número é maior.')
elif numero_1 < numero_2:
    print('O segundo número é maior.')
else:
    print('São números iguais.')
