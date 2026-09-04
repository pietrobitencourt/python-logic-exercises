# 6) Aprovação por nota. Leia a nota de um aluno (0 a 10). Se for maior ou igual a 7, exiba "Aprovado!".

nota = float(input('Digite a sua nota: '))
if 7 <= nota <= 10:
    print('Aprovado!')
else:
    print('Reprovado!')
