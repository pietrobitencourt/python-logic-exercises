# 13) Aprovado ou reprovado. Leia a nota de um aluno (0 a 10). Exiba "Aprovado" se a nota for ≥ 7 ou "Reprovado" caso contrário.

nota = float(input('Digite a sua nota: '))
if 7 <= nota <= 10:
    print('Aprovado!')
else:
    print('Reprovado!')
