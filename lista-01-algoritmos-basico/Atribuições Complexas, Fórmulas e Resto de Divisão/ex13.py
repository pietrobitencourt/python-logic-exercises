# 13. Reajuste Salarial: Faça um algoritmo que leia o salário atual de um funcionário e aplique um aumento de 15%. Exiba o valor do aumento numérico e o novo salário.

salario_atual = float(input('Qual o seu salário atual? '))
aumento = float(input('Qual o percentual de aumento pretendido (%)? '))
novo_salario = salario_atual + (salario_atual * (aumento / 100))
print(f'O seu salário de R${salario_atual:.2f} terá um aumento percentual de {aumento:.0f}%, tendo como reajuste um novo salário de R${novo_salario:.2f}. ')
