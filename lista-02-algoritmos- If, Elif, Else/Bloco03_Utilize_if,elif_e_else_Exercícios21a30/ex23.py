# 23) Faixa etária. Leia a idade e classifique: Criança (0–11), Adolescente (12–17), Adulto (18–59) ou Idoso (60+).

try:
    idade = int(input('Qual a sua idade? '))

    if idade < 0:
            print('Idade inválida!')
    elif idade <= 11:
            print('Criança')
    elif idade <= 17:
            print('Adolescente')
    elif idade <= 59:
            print('Adulto')
    else:
            print('Idoso')

except ValueError:
    print('Digite um valor inteiro!')