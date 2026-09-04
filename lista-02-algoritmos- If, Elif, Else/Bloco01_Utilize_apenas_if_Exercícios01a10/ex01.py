# 1) Verificar maioridade. Leia a idade de uma pessoa e exiba "Você é maior de idade." caso ela tenha 18 anos ou mais.

idade = int(input('Qual a sua idade? '))
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')