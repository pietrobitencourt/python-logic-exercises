# 15) Maior entre dois. Leia dois números e exiba qual é o maior. Se forem iguais, informe que são iguais.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print(f'{numero1} é o maior número!')
elif numero2 > numero1:
    print(f'{numero2} é o maior número!')
else:
    print('São números iguais!')
