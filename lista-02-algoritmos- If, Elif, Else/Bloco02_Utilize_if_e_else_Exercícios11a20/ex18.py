# 18) Ano bissexto completo. Leia um ano e informe se é bissexto ou não bissexto.

ano = int(input('Digite o ano: '))
if ano < 0:
    print('Esse ano não existe!')
elif (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')