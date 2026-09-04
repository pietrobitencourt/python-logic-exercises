# 26) Calculadora simples. Leia dois números e um operador (+, -, *, /).
# Exiba o resultado da operação. Trate a divisão por zero e operador inválido.

try:
    print('-----CALCULADORA SIMPLES-----')
    print('Operadores: [ + ], [ - ], [ * ], [ / ]')

    digito1 = float(input('Digite o primeiro valor: '))
    operador = input('Digite o operador: ')
    digito2 = float(input('Digite o segundo valor: '))

    print('-=-'*10)

    if operador == '+':
        print(f'{digito1} + {digito2} = {digito1 + digito2}')
    elif operador == '-':
        print(f'{digito1} - {digito2} = {digito1 - digito2}')
    elif operador == '*':
        print(f'{digito1} * {digito2} = {digito1 * digito2}')
    elif operador == '/':
        if digito2 == 0:
            print('Erro: Não é possível dividir por 0')
        else:
            print(f'{digito1} / {digito2} = {digito1 / digito2}')
    else:
        print('Operador invalido')

except ValueError:
    print('Valor invalido')
