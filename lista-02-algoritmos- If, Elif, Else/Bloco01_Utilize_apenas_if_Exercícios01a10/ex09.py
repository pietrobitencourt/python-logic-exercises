# 9) Salário acima do mínimo. Leia o salário de um funcionário. Se for superior a R$ 1.412,00, exiba "Salário acima do mínimo vigente.".

salario = float(input('Digite o seu salário(R$): '))
if salario > 1.412:
    print('Salário acima do mínimo vigente.')
elif salario == 1.412:
        print('Sálario mínimo vigente.')
else:
    print('Salário inferior do mínimo vigente.')
