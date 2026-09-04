# 10) Ano bissexto (simplificado). Leia um ano e exiba "Ano bissexto!" se ele for divisível por 4 e (não divisível por 100 ou divisível por 400).

ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')
