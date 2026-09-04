# 8) Divisível por 5. Leia um número inteiro e exiba "Divisível por 5." se a condição for verdadeira.

numero = int(input('Digite um número: '))
if numero % 5 == 0:
    print('Divisível por 5.')
else:
    print('Não divisível por 5.')
