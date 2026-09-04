# 15. Cálculo de Salário Líquido: Leia o salário bruto de um profissional e calcule o desconto de 8% referente ao INSS. Exiba o valor do desconto e o salário líquido restante.

salario_bruto = float(input('Digite o seu salário bruto: R$'))
percentual = int(input('Quantos % de desconto? '))
desconto_inss =  salario_bruto * (percentual / 100)
salario_liquido = salario_bruto - desconto_inss
print(f'O valor descontado foi de R${desconto_inss:.2f} e seu salário líquido atual é de R${salario_liquido:.2f}.')
