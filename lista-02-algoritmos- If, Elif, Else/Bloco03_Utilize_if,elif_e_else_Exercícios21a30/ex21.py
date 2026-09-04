# 21) Classificação por nota (conceito). Leia a nota (0 a 10) e exiba o conceito: A (≥ 9), B (≥ 7), C (≥5), D (≥ 3) ou F (abaixo de 3).

nota = float(input('Insira a sua nota (0 a 10): '))

if nota < 0 or nota > 10:
    print('Nota inválida! Digite um valor entre 0 e 10.')
elif nota >= 9:
    print('Conceito: A')
elif nota >= 7:
    print('Conceito: B')
elif nota >= 5:
    print('Conceito: C')
elif nota >= 3:
    print('Conceito: D')
else:
    print('Conceito: F')
