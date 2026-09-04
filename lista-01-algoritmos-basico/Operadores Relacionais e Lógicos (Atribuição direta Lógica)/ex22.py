#22. Saldo Bancário Positivo: Leia o saldo de uma conta corrente. Atribua a uma variável lógica e exiba se a conta está estritamente positiva (maior que zero).

conta_corrente = float(input('Digite o saldo de sua conta corrente:R$ '))
if conta_corrente > 0:
    print(f'R${conta_corrente:.2f}: Saldo positivo')
else:
    print(f'R${conta_corrente:.2f}: Saldo negativo')
